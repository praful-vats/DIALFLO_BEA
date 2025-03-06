from app.repository.interaction_repo import save_interaction
from app.core.redis_cache import get_cached_response, cache_response
from app.workers.tasks import process_new_order
from sqlalchemy.orm import Session
from app.schemas.query import QueryResponse

# Predefined responses for different types of queries
PREDEFINED_RESPONSES = {
    "order_status": "Your order is on the way. It will arrive in 20 minutes.",
    "new_order": "Please provide your name and phone number to proceed.",
    "general": "How can I assist you today?"
}

# Classify the query based on the text content
def classify_query(text: str) -> str:
    if "where is my order" in text.lower():
        return "order_status"
    elif "i want to place a new order" in text.lower():
        return "new_order"
    return "general"

# Handle the incoming query request
def handle_query(request, db: Session) -> QueryResponse:
    # Check if the response is already cached
    cached_response = get_cached_response(request.query)
    if cached_response:
        return cached_response  

    # Classify the query and get the appropriate response
    query_type = classify_query(request.query)
    response_text = PREDEFINED_RESPONSES.get(query_type, "I'm not sure how to help with that.")

    # If it's a new order, process it asynchronously
    if query_type == "new_order":
        process_new_order.delay({"customer_id": request.customer_id, "query": request.query})

    # Save the interaction in the database
    interaction = save_interaction(db, request.customer_id, request.query, query_type, response_text)

    # Cache the response for future use
    interaction_dict = interaction.as_dict()
    cache_response(request.query, interaction_dict)

    # Return the response as a QueryResponse object
    return QueryResponse(**interaction_dict)
