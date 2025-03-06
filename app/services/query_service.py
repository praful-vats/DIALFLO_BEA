from app.repository.interaction_repo import save_interaction
from app.core.redis_cache import get_cached_response, cache_response
from app.workers.tasks import process_new_order
from sqlalchemy.orm import Session
from app.schemas.query import QueryResponse

PREDEFINED_RESPONSES = {
    "order_status": "Your order is on the way. It will arrive in 20 minutes.",
    "new_order": "Please provide your name and phone number to proceed.",
    "general": "How can I assist you today?"
}

def classify_query(text: str) -> str:
    if "where is my order" in text.lower():
        return "order_status"
    elif "i want to place a new order" in text.lower():
        return "new_order"
    return "general"

def handle_query(request, db: Session) -> QueryResponse:
    cached_response = get_cached_response(request.query)
    if cached_response:
        return cached_response  

    query_type = classify_query(request.query)
    response_text = PREDEFINED_RESPONSES.get(query_type, "I'm not sure how to help with that.")

    if query_type == "new_order":
        process_new_order.delay({"customer_id": request.customer_id, "query": request.query})

    interaction = save_interaction(db, request.customer_id, request.query, query_type, response_text)

    interaction_dict = interaction.as_dict()
    cache_response(request.query, interaction_dict)

    return QueryResponse(**interaction_dict)
