from queue import Queue
from stack import Stack
from calculator import Calculator


def test():
    stack = Stack()
    queue = Queue()

    items = ["Item 1", "Item 2", "Item 3", "Item 4"]
    for item in items:
        stack.push(item)
        queue.push(item)
    print("------------------ Queue test -------------------")
    while queue.size() > 0:
        print(queue.pop())
        print(f"Items left: {queue.size()}")
    print("")
    print("------------------ Stack test -------------------")
    while stack.size() > 0:
        print(stack.pop())
        print(f"Items left: {stack.size()}")


def main():
    """lmao"""
    test_part_4()
    test_part_5()
    test_part_6()
    test_part_7()
    test_part_8()


def test_part_4():
    calc = Calculator()
    print("test calc", calc.functions['EXP'].execute(
        calc.operators['ADD'].execute(
            1, calc.operators['MULTIPLY'].execute(2, 3, debug=False), debug=False), debug=False))


def test_part_5():
    calc = Calculator()
    calc.output_queue.push(1)
    calc.output_queue.push(2)
    calc.output_queue.push(3)
    calc.output_queue.push(calc.operators['MULTIPLY'])
    calc.output_queue.push(calc.operators['ADD'])
    calc.output_queue.push(calc.functions['EXP'])
    print("test rpn", calc.rpn(False))


def test_part_6():
    calc = Calculator()
    input_queue = Queue()
    list1 = [calc.functions['EXP'], '(', 1, calc.operators['ADD'], 2, calc.operators['MULTIPLY'], 3, ')']

    for elem in list1:
        input_queue.push(elem)

    output_queue = calc.shunting_yard(input_queue)
    # print(output_queue)
    for i in range(output_queue.size()):
        elem = output_queue.pop()
        print(elem)
        calc.output_queue.push(elem)

    # print(calc2.output_queue)
    print("test parser", calc.rpn(False))


def test_part_7():
    calc = Calculator()
    # string = "(1 PLUS 2)"
    string = "EXP (1 add 2 multiply 3)"
    input_queue = calc.parse_text(string)
    print(input_queue)
    rpn_queue = calc.shunting_yard(input_queue)
    print(rpn_queue)
    for i in range(rpn_queue.size()):
        elem = rpn_queue.pop()
        calc.output_queue.push(elem)
    print("Result: ", calc.rpn(False))


def test_part_8():
    calc = Calculator()
    string1 = "EXP (1 add 2 multiply 3)"
    string2 = "((15 DIVIDE (7 SUBTRACT (1 ADD 1))) MULTIPLY 3) SUBTRACT (2 ADD (1 ADD 1))"
    print(calc.parse_text(string2))
    print("Result 1: ", calc.calculate_expression(string1))
    print("Result 1: ", calc.calculate_expression(string2))


if __name__ == '__main__':
    main()
