from app.models.interaction import Interaction
from sqlalchemy.orm import Session

def save_interaction(db: Session, customer_id: int, query: str, query_type: str, response: str) -> Interaction:
    # Create a new Interaction object with the provided data
    interaction = Interaction(
        customer_id=customer_id,
        query=query,
        query_type=query_type,
        response=response
    )
    db.add(interaction)
    db.commit()
    db.refresh(interaction)
    return interaction
