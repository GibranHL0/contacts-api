"""Provides all the logic behind the endpoint's operations."""


from Errors import errors
from Factory.contact_factory import ContactFactory
from Validation import validation
from Models.contacts import Contact
from new_app import db, app
from Repository.repository import SQLAlchemyRepository
from typing import List


def create_contact(contact_dict: dict) -> Contact:
    """
    Create a new contact.

    Args:
        contact_dict: Dictonary that contains all the Contact attributes.

    Returns:
        Contact created object.

    Raises:
        EmailAlreadyExists: Indicate that the email is not unique.
        InternalError: Indicate that something unexpected happened.
    """
    repo = SQLAlchemyRepository(db.session)

    # Validate if the contact email exists, raise an exception if so.
    if validation.check_contact_exist(contact_dict.get('email'), repo):
        raise errors.EmailAlreadyExists

    # Validate the contact information. Otherwise raise an exception.
    validation.validate_contact(contact_dict)

    factory = ContactFactory()
    new_contact = factory.create(contact_dict)

    try:
        repo.addcontact(new_contact)

    except Exception as error:
        app.logger.error(error)
        raise errors.InternalError

    return new_contact


def update_contact(email: str, contact: dict) -> Contact:
    """
    Update an existent contact.

    Args:
        email: Previous email of the contact to be updated.
        contact: Dictionary that contains all the Contact attributes.

    Returns:
        Contact updated object.

    Raises:
        EmailNotFound: The email is not in the DB and can't be updated.
        InternalError: Indicate that something unexpected happened.
    """
    repo = SQLAlchemyRepository(db.session)

    # Validate the contact information. Otherwise raise an exception.
    validation.validate_contact(contact)

    # Validate if the contact email exists, raise an exception if don't.
    if not validation.check_contact_exist(contact.get('email'), repo):
        raise errors.EmailNotFound

    # Updates the contact.
    try:
        repo.updatecontact(email, contact)

    except Exception as error:
        app.logger.error(error)
        raise errors.InternalError

    # Creates the factory to create the contact object for the response.
    contact_factory = ContactFactory()

    return contact_factory.create(contact)


def delete_contact(email: str) -> None:
    """
    Delete an existent contact.

    Args:
        email: email of the contact to be deleted.

    Raises:
        EmailNotFound: When the contact is not in the db
        InternalError: Indicate that something unexpected happened.
    """
    repo = SQLAlchemyRepository(db.session)

    # Verify if the email exists.
    if not validation.check_contact_exist(email, repo):
        raise errors.EmailNotFound

    # Delete the contact
    try:
        repo.deletecontact(email)

    except Exception as error:
        app.logger.error(error)
        raise errors.InternalError


def obtain_contacts(quantity: int) -> List[Contact]:
    """
    Obtain the quantity of contacts specified.

    Args:
        quantity: Number of Contacts to be retrieved.

    Returns:
        List of Contacts.

    Raises:
        InternalError: Indicate that something unexpected happened.
    """
    try:
        contacts_data = SQLAlchemyRepository(db.session).getcontacts(quantity)
    except Exception as error:
        app.logger.error(error)
        raise errors.InternalError

    contacts_list = []

    if contacts_data:
        contacts_list = [contact.serialize() for contact in contacts_data]

    return contacts_list
