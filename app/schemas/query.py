from pydantic import BaseModel

class QueryRequest(BaseModel):
    customer_id: int
    query: str

class QueryResponse(BaseModel):
    customer_id: int
    query: str
    query_type: str
    response: str
