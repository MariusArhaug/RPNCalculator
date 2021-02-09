"""Queue data structure"""
from container import Container


class Queue(Container):
    """Inherits from Container"""

    def peek(self):
        """
        Return first element without deleting it
        :return: first element
        """
        assert not self.is_empty()
        return self._items[0]

    def pop(self):
        """
        Pop the first element
        :return: first element
        """
        assert not self.is_empty()
        return self._items.pop(0)
