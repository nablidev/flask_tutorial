from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.secret_key = 'secret'
    app.permanent_session_lifetime = timedelta(days=5)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Database
    db.init_app(app)

    with app.app_context():
        # Imports
        from . import routes
        # Initialize Global db
        db.create_all()

        return app
