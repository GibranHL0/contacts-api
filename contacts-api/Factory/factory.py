"""Defines the contract for the Factory type classes."""

from abc import ABC, abstractmethod


class Factory(ABC):
    """
    Base class for Factory type classes.

    The Factory class declares the creator method that
    is supposed to return an object of a Product class.
    """

    @abstractmethod
    def create(self):
        """
        Create the object.

        The subclasses should provide the implementation
        for the specific object.
        """
