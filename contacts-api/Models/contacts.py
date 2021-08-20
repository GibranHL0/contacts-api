"""Module that defines the contact model."""

from new_app import db

MAX_STRING = 40
MAX_PHONE = 20


class Contact(db.Model):
    """Defines the Contact class."""

    __tablename__ = 'contacts'

    email = db.Column(db.String(), primary_key=True)
    name = db.Column(db.String(MAX_STRING), nullable=False)
    last_name = db.Column(db.String(MAX_STRING), nullable=False)
    company = db.Column(db.String(MAX_STRING), nullable=True)
    phone = db.Column(db.String(MAX_PHONE), nullable=True)

    def __init__(self, contact: dict) -> None:
        """
        Instances the Contacts Model.

        Args:
            contact: Dictionary that contains all the fields for a contact.

        """
        self.name = contact.get('name')
        self.last_name = contact.get('last_name')
        self.company = contact.get('company')
        self.phone = contact.get('phone')
        self.email = contact.get('email')

    @property
    def serialize(self) -> dict:
        """
        Serialize the Contact object into a dictionary.

        Returns:
            A dictionary with all the attributes of the Contact.
        """
        return {
            'email': self.email,
            'name': self.name,
            'last_name': self.last_name,
            'company': self.company,
            'phone': self.phone,
        }

    @property
    def getemail(self) -> str:
        """
        Give the email value of the class.

        Returns:
            email of the Contact
        """
        return self.email
