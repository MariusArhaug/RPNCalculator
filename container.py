"""Container superclass"""
from abc import ABC, abstractmethod


class Container(ABC):
    """
    Super class for Queue and Stack
    """

    def __init__(self):
        self._items = []

    def size(self):
        """
        Get number of items
        :return: int number of items
        """
        return len(self._items)

    def is_empty(self):
        """
        check if size > 0
        :return: boolean
        """
        return self.size() == 0

    def push(self, item):
        """
        Push items into list
        :param item:
        :return: None
        """
        self._items.append(item)

    def __str__(self):
        return str(self._items)

    @abstractmethod
    def pop(self):
        """Get item from list"""

    @abstractmethod
    def peek(self):
        """See item"""
