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

# Running the app
import logging
from logging.handlers import RotatingFileHandler
from waitress import serve

# Configure logging
log_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
log_handler = RotatingFileHandler('app.log', maxBytes=10000000, backupCount=5)
log_handler.setLevel(logging.ERROR)  # Log only errors and above
log_handler.setFormatter(log_formatter)
app.logger.addHandler(log_handler)


# Error handler for HTTP 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error('Server Error: %s', error)
    return 'Internal Server Error', 500


# Error handler for unhandled exceptions
@app.errorhandler(Exception)
def unhandled_exception(error):
    app.logger.exception('Unhandled Exception: %s', error)
    return 'An unexpected error occurred', 500





if __name__ == '__main__':
    DEBUG = str_to_bool(os.environ.get("DEBUG_MODE"))
    PORT = int(os.environ.get("PORT"))
    API_URI = os.environ.get("DEV_URI") if DEBUG else os.environ.get("PROD_URI")

    if DEBUG:
        app.run(debug=DEBUG, host=API_URI, port=PORT)
    else:
        serve(app, host=API_URI, port=PORT)
