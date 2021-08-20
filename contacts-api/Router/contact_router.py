"""Request handler for the Contact endpoint."""

from Errors import errors
from Factory.message_factory import MessageFactory
from flask import request, make_response, jsonify
from flask.wrappers import Response
from new_app import app
from Services import contact_service

OK = 200
PARTIAL_CONTENT = 206
INTERNAL_ERROR = 500


@app.route('/contacts', methods=['POST'])
def create_contact() -> Response:
    """
    Create a new contact.

    Returns:
        Response including a message and HTTP status code.
    """
    contact_dict = request.get_json()
    message_factory = MessageFactory()

    try:
        created_contact = contact_service.create_contact(contact_dict)

    except errors.EmailAlreadyExists:
        message = message_factory.create('Email already exists')
        response = make_response(message.serialize(), PARTIAL_CONTENT)

    except errors.EmailNotValid:
        message = message_factory.create('Email is not valid')
        response = make_response(message.serialize(), PARTIAL_CONTENT)

    except errors.NameNotValid:
        message = message_factory.create('Name is not valid')
        response = make_response(message.serialize(), PARTIAL_CONTENT)

    except errors.LastNameNotValid:
        message = message_factory.create('Last Name is not valid')
        response = make_response(message.serialize(), PARTIAL_CONTENT)

    except Exception as error:
        print(error)
        message = message_factory.create('Something wrong happened')
        response = make_response(message.serialize(), INTERNAL_ERROR)

    else:
        response = make_response(created_contact.serialize(), OK)

    return response


@app.route('/contacts/<quantity>', methods=['GET'])
def obtain_contact(quantity: int) -> Response:
    """
    Obtain contacts.

    Args:
        quantity: Amount of results to be returned.

    Returns:
        Response including a message and HTTP status code.
    """
    message_factory = MessageFactory()

    try:
        contacts_list = contact_service.obtain_contact(quantity)

    except Exception:
        message = message_factory.create('Something wrong happened')
        response = make_response(message.serialize(), INTERNAL_ERROR)

    else:
        response = make_response(jsonify(contacts_list), OK)

    return response
