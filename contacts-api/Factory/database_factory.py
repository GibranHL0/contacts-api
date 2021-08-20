"""Defines the Factory Class for the DB components."""

from Factory.factory import Factory
from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy


class DBFactory(Factory):
    """Creates Db objects."""

    def __init__(self, app: Flask) -> None:
        """
        Instances the DB to use.

        Args:
            app: Flask object.
        """
        self.db = SQLAlchemy(app)

    def create(self) -> SQLAlchemy:
        """
        Create an instance of a db.

        Returns:
            SQLAlchemy object.
        """
        self.db.create_all()
        self.db.session.commit()
        return self.db
