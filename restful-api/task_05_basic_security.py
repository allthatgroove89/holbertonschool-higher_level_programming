from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required, create_access_token, get_jwt
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'
auth = HTTPBasicAuth()
jwt = JWTManager(app)


users = {
    "user1": {"username": "user1", "password": generate_password_hash
              ("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash
               ("password"), "role": "admin"}
}


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    user = users.get(username, None)
    if user and check_password_hash(user['password'], password):
        token = create_access_token(
            identity=username, additional_claims={"role": user["role"]})
        return jsonify(access_token=token), 200
    else:
        return jsonify({"msg": "Bad username or password"}), 401


@auth.verify_password
def verify_password(username, password):
    user = users.get(username, None)
    if user and check_password_hash(user['password'], password):
        return username


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return jsonify(message="Basic Auth: Access Granted"), 200


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return jsonify(message="JWT Auth: Access Granted"), 200


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    claims = get_jwt()
    if claims['role'] != 'admin':
        return jsonify({"msg": "Access forbidden"}), 403
    return jsonify(message="Admin Access: Granted"), 200


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run(debug=True)
