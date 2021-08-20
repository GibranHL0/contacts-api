"""Defines the Contact Class factory."""

from Factory.factory import Factory
from Models.contacts import Contact


class ContactFactory(Factory):
    """Creates a Contact Object."""

    def create(self, contact: dict) -> Contact:
        """
        Instances a new Contact object.

        Args:
            contact: Dictonary that contains all the attributes of a contact.

        Returns:
            Contact object.
        """
        return Contact(contact)
