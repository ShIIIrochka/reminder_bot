import redis

user_connection = redis.Redis(host="0.0.0.0", port=6378, decode_responses=True)
