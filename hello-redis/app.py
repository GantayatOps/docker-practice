from flask import Flask
import os
import redis

app = Flask(__name__)

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

# decode_responses=True so Redis returns strings, not bytes
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, decode_responses=True)

@app.route("/")
def index():
    try:
        count = r.incr("hits")
        return f"Hello from Flask! Visit count: {count}"
    except Exception as e:
        return f"Hello from Flask! (Redis unavailable: {e})"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

