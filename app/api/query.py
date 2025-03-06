from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.query import QueryRequest, QueryResponse
from app.services.query_service import handle_query
from app.core.database import get_db

# Initialize the API router with a prefix and tags for the query endpoint
router = APIRouter(prefix="/query", tags=["Query"])

@router.post("/", response_model=QueryResponse, status_code=status.HTTP_200_OK)
def process_query(request: QueryRequest, db: Session = Depends(get_db)):
    """
    Endpoint to process a query request.
    - request: The query request payload.
    - db: Database session dependency.
    """
    try:
        # Handle the query using the query service
        interaction = handle_query(request, db)
        return interaction
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
