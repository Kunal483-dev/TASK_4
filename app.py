from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user storage
users = {
    1: {"id": 1, "name": "Raj", "email": "raj@example.com"},
    2: {"id": 2, "name": "Amit", "email": "amit@example.com"}
}

next_user_id = 3


# GET: Get all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(list(users.values())), 200


# GET: Get one user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user), 200


# POST: Create a new user
@app.route("/users", methods=["POST"])
def create_user():
    global next_user_id

    data = request.get_json()

    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Name and email are required"}), 400

    new_user = {
        "id": next_user_id,
        "name": data["name"],
        "email": data["email"]
    }

    users[next_user_id] = new_user
    next_user_id += 1

    return jsonify(new_user), 201


# PUT: Update an existing user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = users.get(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    user["name"] = data.get("name", user["name"])
    user["email"] = data.get("email", user["email"])

    return jsonify(user), 200


# DELETE: Delete a user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = users.get(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    del users[user_id]

    return jsonify({"message": "User deleted successfully"}), 200


if __name__ == "__main__":
    app.run(debug=True,port=5500)