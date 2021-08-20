"""Repository that performs all data base actions."""

from abc import ABC, abstractmethod
from typing import List

from Models.contacts import Contact
from sqlalchemy.orm.scoping import scoped_session


class AbstractRepository(ABC):
    """Base repository for all DBs."""

    @abstractmethod
    def addcontact(self, contact: Contact):
        """
        Add a new Contact.

        Args:
            contact: The contact db.Model
        """

    @abstractmethod
    def getcontact(self, email: str) -> Contact:
        """
        Retrieve a Contact by the email given.

        Args:
            email: The email of the Contact to be obtained.
        """

    @abstractmethod
    def getcontacts(self, quantity: int) -> List[Contact]:
        """
        Retrieve all the Contacts according to the quantity.

        Args:
            quantity: The number of contacts to be retrieved.
        """

    @abstractmethod
    def updatecontact(self, email: str, contact: Contact) -> Contact:
        """
        Update the Contact information.

        Args:
            email: The email of the contact to be updated.
            contact: Contact to be updated.
        """

    @abstractmethod
    def deletecontact(self, email: str) -> Contact:
        """
        Delete a Contact.

        Args:
            email: The email of the contact to be deleted.
        """


class SQLAlchemyRepository(AbstractRepository):
    """Repository for the SQLAlchemy ORM."""

    def __init__(self, session: scoped_session) -> None:
        """
        Start a new session in the DB.

        Args:
            session: Database object from the SQLAlchemy
        """
        self.session = session

    def addcontact(self, contact: Contact):
        """
        Add a new Contact with SQLAlchemy.

        Args:
            contact: Contact to be added in the DB.
        """
        self.session.add(contact)
        self.session.commit()

    def getcontact(self, email: str) -> Contact:
        """
        Retrieve a Contact by the email given.

        Args:
            email: The email of the Contact to be obtained.

        Returns:
            Contact or None according to its existance
        """
        return self.session.query(Contact).get(email)

    def getcontacts(self, quantity: int) -> List[Contact]:
        """
        Obtain the quantity of contacts defined.

        Args:
            quantity: Number of contacts to be retrieved.

        Returns:
            Return a list of Contact
        """
        return self.session.query(Contact).limit(quantity).all()

    def updatecontact(self, email: str, contact: dict) -> Contact:
        """
        Update a Contact info.

        Args:
            email: Email of the contact to be updated.
            contact: Dict containing all the elements to be updated
        """
        self.session.query(Contact).filter(
            Contact.email == email,
        ).update(contact)
        self.session.commit()

    def deletecontact(self, email: str) -> Contact:
        """
        Delete a Contact info.

        Args:
            email: Email of the contact to be deleted.
        """
        self.session.query(Contact).filter(
            Contact.email == email,
        ).delete(synchronize_session=False)
        self.session.commit()
