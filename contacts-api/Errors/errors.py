"""Define contact-api defined exceptions."""

from abc import ABC
from http import HTTPStatus


class Error(ABC, Exception):
    """Base error class raised when a custom error happened."""

    def __init__(
        self,
        message='',
        code=HTTPStatus.INTERNAL_SERVER_ERROR,
    ) -> None:
        """
        Initialize the exception.

        Args:
            message: Explanation of the error.
            code: HTTP code error.
        """
        self.msg = message
        self.code = code
        super().__init__(self.msg)


class EmailNotValid(Error):
    """Exception raised when the email is not valid."""

    def __init__(
        self,
        message='Email is not valid',
        code=HTTPStatus.PARTIAL_CONTENT,
    ) -> None:
        """
        Inititalize the exception.

        Args:
            message: Explanation of the error.
            code: HTTP code error.
        """
        self.msg = message
        self.code = code
        super().__init__(self.msg, self.code)


class EmailNotFound(Error):
    """Exception raised when the email is not found in the DB."""

    def __init__(
        self,
        message='Email not found',
        code=HTTPStatus.PARTIAL_CONTENT,
    ) -> None:
        """
        Inititalize the exception.

        Args:
            message: Explanation of the error.
            code: HTTP code error.
        """
        self.msg = message
        self.code = code

        super().__init__(self.msg, self.code)


class EmailAlreadyExists(Error):
    """Exception raised when the email is already in the Contacts list."""

    def __init__(
        self,
        message='Email already exists',
        code=HTTPStatus.PARTIAL_CONTENT,
    ) -> None:
        """
        Initialize the exception.

        Args:
            message: Explation of the error.
            code: HTTP error code.
        """
        self.msg = message
        self.code = code

        super().__init__(self.msg, self.code)


class NameNotValid(Error):
    """Exception raised when the name is not in the appropiate format."""

    def __init__(
        self,
        message='Name is not valid',
        code=HTTPStatus.PARTIAL_CONTENT,
    ) -> None:
        """
        Initialize the exception.

        Args:
            message: Explanation of the error.
            code: HTTP error code.
        """
        self.msg = message
        self.code = code

        super().__init__(self.msg, self.code)


class LastNameNotValid(Error):
    """Exception raised when the last name is not in the appropiate format."""

    def __init__(
        self,
        message='Last name is not valid',
        code=HTTPStatus.PARTIAL_CONTENT,
    ) -> None:
        """
        Initialize the exception.

        Args:
            message: Explanation of the error.
            code: HTTP error code.
        """
        self.msg = message
        self.code = code

        super().__init__(self.msg, self.code)


class InternalError(Error):
    """Exception raised when something unexpected happened."""

    def __init__(
        self,
        message='Something wrong happened',
        code=HTTPStatus.INTERNAL_SERVER_ERROR,
    ) -> None:
        """
        Initialize the exception.

        Args:
            message: Explanation of the error.
            code: HTTP error code.
        """
        self.msg = message
        self.code = code

        super().__init__(self.msg, self.code)
