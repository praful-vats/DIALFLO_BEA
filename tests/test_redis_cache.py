import json
from unittest.mock import MagicMock
from app.core.redis_cache import get_cached_response, cache_response

def test_cache_response(monkeypatch):
    mock_redis = MagicMock()
    monkeypatch.setattr("app.core.redis_cache.redis_client", mock_redis)

    query = "Where is my order?"
    response = {"query": query, "response": "On the way!"}

    cache_response(query, response)
    mock_redis.setex.assert_called_with(query, 3600, json.dumps(response))

def test_get_cached_response(monkeypatch):
    mock_redis = MagicMock()
    monkeypatch.setattr("app.core.redis_cache.redis_client", mock_redis)

    query = "Where is my order?"
    response = {"query": query, "response": "On the way!"}
    mock_redis.get.return_value = json.dumps(response)

    cached = get_cached_response(query)
    assert cached == response
