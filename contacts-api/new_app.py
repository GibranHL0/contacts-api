"""Initialize the project."""

from Factory.app_factory import flask_app
from Factory.database_factory import DBFactory

app = flask_app
db = DBFactory(app).create()

# All the view functions (the ones with a route() decorator on top) have
# to be imported in the __init__.py file. Not the object itself, but the
# module it is in. Import the view module after the application object is
# created.
from Router import contact_router

if __name__ == 'main':
    app.run(debug=True)
