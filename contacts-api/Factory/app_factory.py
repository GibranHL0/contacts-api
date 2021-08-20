"""Defines the Factory Class for the app component."""

from config import Config
from Factory.factory import Factory
from flask import Flask
from flask_cors import CORS


class AppFactory(Factory):
    """Creates App Objects."""

    def __init__(self) -> None:
        """Instances the app object."""
        self.app = Flask(__name__)

    def create(self) -> Flask:
        """
        Return the created app.

        Returns:
            Flask instance.
        """
        self.apply_cors()
        self.apply_config()
        return self.app

    def apply_cors(self) -> None:
        """Apply CORS policy into the app."""
        CORS(self.app, resources={'/*': {'origins': '*'}})

    def apply_config(self) -> None:
        """Apply the configuration into the app."""
        self.app.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URI
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
