from flask import Blueprint
# from controllers.user import create, update, delete

root = Blueprint('root', __name__)

root.get("/")(lambda: "Hello World")
