from flask import Blueprint, jsonify

my_blueprint = Blueprint("my_blueprint", __name__)

@my_blueprint.route("/", methods=["GET"])
def api_route():
    data = {"message": "Hello from Blueprint API!"}
    return jsonify(data)