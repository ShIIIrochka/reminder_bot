import redis

user_connection = redis.Redis(host="0.0.0.0", port=6378)
user_connection.ping()
