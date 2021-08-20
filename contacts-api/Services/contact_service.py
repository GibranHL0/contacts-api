"""Provides all the logic behind the endpoint's operations."""

from Errors import errors
from Factory.contact_factory import ContactFactory
from Logic import validation
from Models.contacts import Contact
from new_app import db
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
        EmailAlreadyExists: Raise when the email is already on Contacts list.
    """
    repo = SQLAlchemyRepository(db.session)

    # Validate if the contact email is already in the DB
    exists = validation.check_contact_exist(contact_dict.get('email'), repo)

    if exists:
        raise errors.EmailAlreadyExists(contact_dict.get('email'))

    # Validate the contact information. Otherwise raise an exception.
    validation.validate_contact(contact_dict)

    factory = ContactFactory()
    new_contact = factory.create(contact_dict)
    repo.addcontact(new_contact)

    return new_contact


def obtain_contact(quantity: int) -> List[Contact]:
    """
    Obtain the quantity of contacts specified.

    Args:
        quantity: Number of Contacts to be retrieved.

    Returns:
        List of Contacts.
    """
    contacts_data = SQLAlchemyRepository(db.session).getcontacts(quantity)
    contacts_list = []

    if contacts_data:
        contacts_list = [contact.serialize for contact in contacts_data]

    return contacts_list
