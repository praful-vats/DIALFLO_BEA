import redis
import json
from app.core.config import settings

# Initialize Redis client with settings from configuration
redis_client = redis.Redis(
    host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0, decode_responses=True
)

def get_cached_response(query: str):
    try:
        # Attempt to retrieve cached response from Redis
        response = redis_client.get(query)
        return json.loads(response) if response else None
    except redis.RedisError as e:
        print(f"Redis error: {e}")
        return None  # Fallback if Redis is unavailable

def cache_response(query: str, response: dict):
    try:
        # Cache the response in Redis with a 1-hour expiration
        redis_client.setex(query, 3600, json.dumps(response))
    except redis.RedisError as e:
        print(f"Redis cache error: {e}")
