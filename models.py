import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = app.app
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class UsersModel(db.Model):
    __tablename__ = 'users'

    email = db.Column(db.String(),primary_key=True)

class ContactsModel(db.Model):
    __tablename__ = 'cars'