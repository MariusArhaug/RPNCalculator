"""
Imports
"""
import numbers
import numpy


class Operator:  # pylint: disable=too-few-public-methods
    """Operator class, do an operation between two elements and decide the strength of operator"""

    def __init__(self, operation, strength):
        self.operation = operation
        self.strength = strength

    def execute(self, element_1, element_2, debug=True):
        """
        Execute function call with element
        :param element_1:
        :param element_2:
        :param debug:
        :return: function of element f(e)
        """
        # result = 0
        # Check type
        if not isinstance(element_1, numbers.Number) and not isinstance(element_2, numbers.Number):
            raise TypeError("The element must be a number")

        if isinstance(element_1, Operator):
            # Check strength
            pass
        elif isinstance(element_2, Operator):
            pass

        result = self.operation(element_1, element_2)

        # Report
        if debug:
            print(f"Function {self.operation.__name__} {element_1, element_2} = {result}")
        return result


def main():
    """lmao"""
    add_op = Operator(operation=numpy.add, strength=0)
    multiply_op = Operator(operation=numpy.multiply, strength=1)
    print(add_op.execute(1, multiply_op.execute(2, 3)))


if __name__ == '__main__':
    main()
