"""Main calculator"""
import numbers
import re
from queue import Queue
import numpy
from stack import Stack
from function import Function
from operator_function import Operator


class Calculator:
    """Calculator class with functions and operators"""

    def __init__(self):
        """
        Define the functions supported
        """
        self.functions = {'EXP': Function(numpy.exp),
                          'LOG': Function(numpy.log),
                          'SIN': Function(numpy.sin),
                          'COS': Function(numpy.cos),
                          'SQRT': Function(numpy.sqrt)}

        # Define operators
        self.operators = {'ADD': Operator(numpy.add, 0),
                          'PLUS': Operator(numpy.add, 0),
                          'MULTIPLY': Operator(numpy.multiply, 1),
                          'TIMES': Operator(numpy.add, 0),
                          'DIVIDE': Operator(numpy.divide, 1),
                          'SUBTRACT': Operator(numpy.subtract, 0),
                          'MINUS': Operator(numpy.add, 0)}

        self.output_queue = Queue()

    def rpn(self, boolean=True):
        """
        Read RPN and calculate result
        :param boolean:
        :return: number
        """
        stack = Stack()
        while self.output_queue.size() > 0:
            # Get next item
            next_item = self.output_queue.peek()
            if isinstance(next_item, numbers.Number):
                # If number, push into stack
                stack.push(self.output_queue.pop())
            elif isinstance(next_item, Function):
                # If function, do function with next element in stack (LIFO)
                next_item = self.output_queue.pop()
                stack_elem = stack.pop()
                calculated_elem = next_item.execute(stack_elem, debug=boolean)
                stack.push(calculated_elem)
            elif isinstance(next_item, Operator):
                # If operator, do operation with two next element in stack
                next_item = self.output_queue.pop()
                stack_elem_one = stack.pop()
                stack_elem_two = stack.pop()
                calculated_elem = next_item.execute(stack_elem_one, stack_elem_two, debug=boolean)
                stack.push(calculated_elem)

        return stack.pop()

    @staticmethod
    def shunting_yard(input_queue):
        """
        Get an input queue of operations, functions and numbers and turn it into RPN notation
        :param input_queue: queue of int, function, operation
        :return: RPN equivalent queue
        """
        operator_stack = Stack()
        output_queue = Queue()

        for i in range(input_queue.size()):  # pylint: disable=unused-variable
            # Check what next element is, without removing it
            elem = input_queue.peek()

            # a)
            if isinstance(elem, numbers.Number):
                output_queue.push(input_queue.pop())
            # b)
            elif isinstance(elem, Function):
                operator_stack.push(input_queue.pop())
            # c)
            elif elem == '(':
                operator_stack.push(input_queue.pop())
            # d)
            elif elem == ')':
                for j in range(operator_stack.size()):  # pylint: disable=unused-variable
                    # Check next element without removing it
                    inner_elem = operator_stack.peek()
                    # print(inner_elem)
                    if inner_elem == '(':
                        # Discard '('
                        operator_stack.pop()
                    else:
                        output_queue.push(operator_stack.pop())

                # Discard elem == ')' as well.
                input_queue.pop()
            # e)
            elif isinstance(elem, Operator):
                for k in range(operator_stack.size()):  # pylint: disable=unused-variable
                    operator = operator_stack.peek()

                    if operator == '(':
                        break
                    if operator.strength < elem.strength:
                        break

                    output_queue.push(operator_stack.pop())
                # Push elem to operator stack
                operator_stack.push(input_queue.pop())
        return output_queue

    def parse_text(self, text_string):
        """
        Parse text string into list of numbers, functions and operations
        :param text_string:
        :return: list of integers functions operations
        """
        string_list = text_string.upper().split(' ')
        input_queue = Queue()
        for word in string_list:
            if re.search("^[-0123456789.()]+", word):
                if re.search('[(]', word):
                    # If word contains '(' we need to push each individually
                    new_number = ""
                    for char in word:
                        if char == '(':
                            input_queue.push(char)
                        else:
                            new_number += char
                    input_queue.push(float(new_number))

                elif re.search('[)]', word):
                    # If word contains ')' we need to push each individually
                    new_number = ""
                    for char in word:
                        if char != ')':
                            new_number += char
                    input_queue.push(float(new_number))
                    for char in word:
                        if char == ')':
                            input_queue.push(char)
                else:
                    input_queue.push(float(word))

            elif re.search('|'.join(['^' + func for func in self.functions]), word):
                input_queue.push(self.functions[word])
            elif re.search('|'.join(['^' + func for func in self.operators]), word):
                input_queue.push(self.operators[word])

        return input_queue

    def calculate_expression(self, txt):
        """
        Input string text of operations and return final value
        :param txt:
        :return:
        """
        input_queue = self.shunting_yard(self.parse_text(txt))
        while input_queue.size() > 0:
            self.output_queue.push(input_queue.pop())
        return self.rpn(False)
