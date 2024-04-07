from flask import Blueprint
from routes.user import user

v1_0 = Blueprint('v1', __name__, url_prefix='/v1')

def v1_0_message():
    return "Welcome to the API v1.0"

v1_0.get("/")(v1_0_message)

v1_0.register_blueprint(user, url_prefix='/user')