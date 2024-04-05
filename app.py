# Importing the necessary modules and libraries
from flask import Flask
# from flask_migrate import Migrate
from routes.user import user
from routes.root import root
# from models.machine import db


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


if __name__ == '__main__':  # Running the app
    app.run(host='127.0.0.1', port=3000, debug=app.config['DEBUG'])