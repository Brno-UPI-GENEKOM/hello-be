from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime, timezone

app = Flask(__name__)
CORS(app)  # allow FE in dev; later restrict origins to your FE domain

@app.get("/")
def hello():
    return "Hello from Flask 👋"

@app.get("/api/time")
def time_now():
    now = datetime.now(timezone.utc).isoformat()
    return jsonify({"utc": now})

if __name__ == "__main__":
    app.run(debug=True)
