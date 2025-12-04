from flask import Flask, jsonify
from db import get_user

app = Flask(__name__)

@app.route("/user/<int:user_id>")
def user_info(user_id):
    user = get_user(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/ping")
def ping():
    return jsonify({"message": "pong"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
