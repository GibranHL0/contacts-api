"""Defines the Message Contact Class factory."""

from Factory.factory import Factory
from Models.message import Message


class MessageFactory(Factory):
    """Create instances of Messages."""

    def create(self, message: str) -> Message:
        """
        Instances a new Message object.

        Args:
            message: Additional information for the response.

        Returns:
            Message object.
        """
        return Message(message)
