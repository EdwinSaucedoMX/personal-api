# Importing the necessary modules and libraries
import os
from dotenv import load_dotenv
from flask import Flask
# from flask_migrate import Migrate
from routes.user import user
from routes.root import root
# from models.machine import db

# Loading the environment variables
load_dotenv()

def create_app():
    app = Flask(__name__)  # flask app object
    app.config.from_object('config')  # Configuring from Python Files
    
    
    # db.init_app(app)  # Initializing the database
    return app


app = create_app()  # Creating the app
# Registering the blueprint
app.register_blueprint(root, url_prefix='/')
app.register_blueprint(user, url_prefix='/user')
# migrate = Migrate(app, db)  # Initializing the migration

DEBUG = os.environ.get("DEBUG_MODE")
API_URI = os.environ.get("DEV_URI") if DEBUG else os.environ.get("PROD_URI")
print(DEBUG)
print(API_URI)


if __name__ == '__main__':  # Running the app
    app.run(host=API_URI, port=3000, debug=DEBUG)