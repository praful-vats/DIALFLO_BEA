from app.services.query_service import classify_query

def test_classify_query():
    assert classify_query("Where is my order?") == "order_status"
    assert classify_query("I want to place a new order") == "new_order"
    assert classify_query("Tell me a joke") == "general"
