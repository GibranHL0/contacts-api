"""Request handler for the Contact endpoint."""

from Errors.errors import Error
from Factory.message_factory import MessageFactory
from flask import request, make_response, jsonify
from flask.wrappers import Response
from http import HTTPStatus
from new_app import app
from Services import contact_service


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

    except Error as error:
        message = message_factory.create(error.msg)
        response = make_response(message.serialize(), error.code)

    else:
        response = make_response(created_contact.serialize(), HTTPStatus.OK)

    return response


@app.route('/contacts/<email>', methods=['PUT'])
def update_contact(email: str) -> Response:
    """
    Update a contact.

    Args:
        email: Previous email of the contact to be updated.

    Returns:
        Response including a message and HTTP status code.
    """
    contact_data = request.get_json()
    message_factory = MessageFactory()

    try:
        updated_contact = contact_service.update_contact(email, contact_data)

    except Error as error:
        message = message_factory.create(error.msg)
        response = make_response(message.serialize(), error.code)

    else:
        response = make_response(updated_contact.serialize(), HTTPStatus.OK)

    return response


@app.route('/contacts/<email>', methods=['DELETE'])
def delete_contact(email: str) -> Response:
    """
    Delete an existent contact.

    Args:
        email: Email of the contact to be deleted.

    Returns:
        Response including a message and HTTP status code.
    """
    message_factory = MessageFactory()

    try:
        contact_service.delete_contact(email)

    except Error as error:
        message = message_factory.create(error.msg)
        response = make_response(message.serialize(), error.code)

    else:
        message = message_factory.create(f'{email} deleted')
        response = make_response(message.serialize(), HTTPStatus.OK)

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
        contacts_list = contact_service.obtain_contacts(quantity)

    except Error as error:
        message = message_factory.create(error.msg)
        response = make_response(message.serialize(), error.code)

    else:
        response = make_response(jsonify(contacts_list), HTTPStatus.OK)

    return response
