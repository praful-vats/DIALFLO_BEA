from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.query import QueryRequest, QueryResponse
from app.services.query_service import handle_query
from app.core.database import get_db

router = APIRouter(prefix="/query", tags=["Query"])

@router.post("/", response_model=QueryResponse, status_code=status.HTTP_200_OK)
def process_query(request: QueryRequest, db: Session = Depends(get_db)):
    try:
        interaction = handle_query(request, db)
        return interaction
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
