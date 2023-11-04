from flask import Blueprint

bp = Blueprint("my_blueprint", __name__)

@bp.route("/")
def index():
    return "Hello from my Blueprint!"