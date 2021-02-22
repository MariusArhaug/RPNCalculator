"""Module of function class"""
import numbers
import numpy


class Function:  # pylint: disable=too-few-public-methods
    """Function class"""

    def __init__(self, func):
        self.func = func

    def execute(self, element, debug=True):
        """
        Execute function call with element
        :param element:
        :param debug:
        :return: function of element f(e)
        """
        # Check type
        if not isinstance(element, numbers.Number):
            raise TypeError("The element must be a number")
        result = self.func(element)

        # Report
        if debug:
            print(f"Function {self.func.__name__} {element, result}")

        return result


def main():
    """Main"""
    exp = Function(numpy.exp)
    sin = Function(numpy.sin)
    print(exp.execute(sin.execute(0)))


if __name__ == '__main__':
    main()
