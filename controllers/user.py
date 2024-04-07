from flask import request
from helpers.assertions import check_fields

def create():
    req = request.get_json()
    if(check_fields(req, required_fields=['name', 'email', 'password'])):
        return check_fields(req, required_fields=['name', 'email', 'password'])
    
    return 'User created'

def update():
    return 'User updated'

def delete():
    return 'User deleted'

# Path: routes/user.py