from pydantic import BaseModel

# Model for the request payload of a query
class QueryRequest(BaseModel):
    customer_id: int
    query: str

# Model for the response payload of a query
class QueryResponse(BaseModel):
    customer_id: int 
    query: str
    query_type: str
    response: str
