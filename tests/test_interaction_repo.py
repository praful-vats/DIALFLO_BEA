from app.repository.interaction_repo import save_interaction
from app.models.interaction import Interaction

def test_save_interaction(db):
    interaction = save_interaction(db, customer_id=1, query="Where is my order?", query_type="order_status", response="Your order is on the way.")
    
    assert interaction.customer_id == 1
    assert interaction.query == "Where is my order?"
    assert interaction.query_type == "order_status"
    assert interaction.response == "Your order is on the way."

    # Ensure it is saved in the database
    retrieved = db.query(Interaction).filter_by(id=interaction.id).first()
    assert retrieved is not None
    assert retrieved.query == "Where is my order?"
