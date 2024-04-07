from flask import Blueprint
from controllers.user import create, update, delete

user = Blueprint('user', __name__)

user.post("/")(create)
