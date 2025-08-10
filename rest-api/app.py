from flask import Flask, jsonify

app = Flask(__name__)

users = {
    "1": {"name": "Windows User", "email": "user@windows.com"},
    "2": {"name": "Admin", "email": "admin@windows.com"}
}

@app.route("/user/<user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id, {"name": "Unknown", "email": "N/A"})
    return jsonify({"user_id": user_id, **user})

if __name__ == "__main__":
    app.run(port=5000)