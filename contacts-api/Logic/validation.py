"""Module that contains multiple validation functions."""

from re import search

from Errors import errors
from Repository.repository import SQLAlchemyRepository


def check_contact_exist(email: str, repository: SQLAlchemyRepository) -> bool:
    """
    Check in the database if the contact already exists.

    Args:
        email: Email of the contact to look up.
        repository: Object to perform the needed data base operations.

    Returns:
        bool value that indicates if the contact was found or not.
    """
    return bool(repository.getcontact(email))


def validate_email(email: str) -> bool:
    """
    Check if the email has a correct format.

    Args:
        email: Email to be checked by regex.

    Returns:
        bool value indicating if the email is valid.
    """
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    return bool(search(regex, email))


def validate_names(name: str) -> bool:
    """
    Check if the name or last name has a correct format.

    Args:
        name: Name or last name to checked by regex

    Returns:
        bool value indicating if the name or last name is valid.
    """
    regex = '^[a-zA-Z_ ]*$'

    return bool(search(regex, name))


def validate_contact(contact: dict) -> None:
    """
    Check if all the attributes have the correct format.

    Args:
        contact: Dictionary that contains all the attributes of a Contact.

    Raises:
        EmailNotValid: Raise when the email does not have an appropiate format.
        NameNotValid: Raise when the name does not have an appropiate format.
        LastNameNotValid: Raise when the last name doesn't comply the format.
    """
    email = contact.get('email')

    # Validate if the email is valid
    valid_email = validate_email(email)

    if not valid_email:
        raise errors.EmailNotValid(email)

    # Validate if the name is correct
    valid_name = validate_names(contact.get('name'))

    if not valid_name:
        raise errors.NameNotValid(contact.get('name'))

    # Validate if the last_name is correct
    valid_last_name = validate_names(contact.get('last_name'))

    if not valid_last_name:
        raise errors.LastNameNotValid
