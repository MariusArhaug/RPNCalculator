from container import Container


class Stack(Container):

    def peek(self):
        """
        Find last item in stack.
        :return:
        """
        assert not self.is_empty()
        return self._items[-1]

    def pop(self):
        """
        Remove first element in stack and return it
        :return: first element
        """
        assert not self.is_empty()
        return self._items.pop()
