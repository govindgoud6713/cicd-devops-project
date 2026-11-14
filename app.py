
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify(
        message="My first Kubernetes rolling update is successful!",
        status="running"
    )

@app.get("/health")
def health():
    return jsonify(status="healthy"), 200

if __name__ == "__main__":
    # 0.0.0.0 makes the app reachable outside this process/container.
    app.run(host="0.0.0.0", port=5000, debug=True)
