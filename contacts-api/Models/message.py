"""Module that defines the message class."""


class Message(object):
    """Defines the message to be added in the response."""

    def __init__(self, message: str) -> None:
        """
        Instances the Message Class.

        Args:
            message: Aditional information of the response.
        """
        self.msg = message

    def serialize(self) -> dict:
        """
        Serialize the Message object into a dictionary.

        Returns:
            A dictionary with the msg of the Message object.
        """
        return {
            'msg': self.msg,
        }
