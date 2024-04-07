# Importing the necessary modules and libraries
import os
from dotenv import load_dotenv
from flask import  Flask
from routes.v1_0 import v1_0
# from flask_migrate import Migrate
# from models.machine import db

# Loading the environment variables
load_dotenv()

def str_to_bool(s):
    return s.lower() in ['true', '1', 't', 'y', 'yes']


def create_app():
    app = Flask(__name__)  # flask app object

    # app.config.from_object('config')  # Configuring from Python Files
    
    # db.init_app(app)  # Initializing the database

    return app



app = create_app()  # Creating the app

app.register_blueprint(v1_0) # Registering version 1.0 of the API

# migrate = Migrate(app, db)  # Initializing the migration

DEBUG = str_to_bool(os.environ.get("DEBUG_MODE"))
PORT = int(os.environ.get("PORT"))
API_URI = os.environ.get("DEV_URI") if (DEBUG) else os.environ.get("PROD_URI")



if __name__ == '__main__':  # Running the app
    app.run(host=API_URI , port=PORT, debug=DEBUG, use_reloader=True)