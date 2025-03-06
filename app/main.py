from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import query
from app.core.database import Base, engine
import redis

app = FastAPI(title="Diaflo_BEA")

# Create database tables
Base.metadata.create_all(bind=engine)

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/api")
def healthcheck():
    return {"status": "ok"}

# Include API router
app.include_router(query.router)

# Redis configuration
redis_host = "localhost"
redis_port = 6379

# Test connection to Redis
@app.get("/test_redis")
def test_redis():
    try:
        r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)
        return {"Redis Ping": r.ping()}
    except Exception as e:
        return {"error": str(e)}