"""Define contact-api defined exceptions."""


class EmailNotValid(Exception):
    """Exception raised when the email is not valid."""

    def __init__(self, email='', message='Email is not valid') -> None:
        """
        Inititalize the exception.

        Args:
            email: Email that raise the exception (optional)
            message: Explanation of the error.
        """
        self.email = email
        self.message = message
        super().__init__(self.message)


class EmailNotFound(Exception):
    """Exception raised when the email is not found in the DB."""

    def __init__(self, email='', message='Email not found') -> None:
        """
        Inititalize the exception.

        Args:
            email: Email that raise the exception (optional)
            message: Explanation of the error.
        """
        self.email = email
        self.message = message

        super().__init__(self.message)


class EmailAlreadyExists(Exception):
    """Exception raised when the email is already in the Contacts list."""

    def __init__(self, email='', message='Email already exists') -> None:
        """
        Initialize the exception.

        Args:
            email: Email that raise the exception (optional)
            message: Explation of the error.
        """
        self.email = email
        self.message = message

        super().__init__(self.message)


class NameNotValid(Exception):
    """Exception raised when the name is not in the appropiate format."""

    def __init__(self, name='', message='Name is not valid') -> None:
        """
        Initialize the exception.

        Args:
            name: Name that raise the exception (optional)
            message: Explanation of the error.
        """
        self.name = name
        self.message = message

        super().__init__(self.message)


class LastNameNotValid(Exception):
    """Exception raised when the last name is not in the appropiate format."""

    def __init__(self, last_name='', message='Last name is not valid') -> None:
        """
        Initialize the exception.

        Args:
            last_name: Name that raise the exception (optional)
            message: Explanation of the error.
        """
        self.last_name = last_name
        self.message = message

        super().__init__(self.message)
