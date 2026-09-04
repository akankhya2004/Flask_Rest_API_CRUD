from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user data as required by the task
users = {
    1: {"id": 1, "name": "Akankhya", "email": "akankhya@example.com"},
    2: {"id": 2, "name": "Rahul", "email": "rahul@example.com"}
}


@app.route("/users", methods=["GET"])
def get_users():
    """Return all users."""
    return jsonify(list(users.values())), 200


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    """Return one user by ID."""
    user = users.get(user_id)

    if user is None:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user), 200


@app.route("/users", methods=["POST"])
def create_user():
    """Create a new user."""
    data = request.json

    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "name and email are required"}), 400

    new_id = max(users.keys(), default=0) + 1

    user = {
        "id": new_id,
        "name": data["name"],
        "email": data["email"]
    }

    users[new_id] = user
    return jsonify(user), 201


@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    """Update an existing user."""
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.json

    if not data:
        return jsonify({"error": "JSON body is required"}), 400

    users[user_id]["name"] = data.get("name", users[user_id]["name"])
    users[user_id]["email"] = data.get("email", users[user_id]["email"])

    return jsonify(users[user_id]), 200


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    """Delete a user by ID."""
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    deleted_user = users.pop(user_id)
    return jsonify({
        "message": "User deleted successfully",
        "user": deleted_user
    }), 200


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Flask User REST API is running",
        "endpoints": [
            "GET /users",
            "GET /users/<id>",
            "POST /users",
            "PUT /users/<id>",
            "DELETE /users/<id>"
        ]
    }), 200


if __name__ == "__main__":
    app.run(debug=True)
