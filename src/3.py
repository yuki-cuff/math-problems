
import random

def get_random_code():
    numbers = list(range(10))
    operators = ["+", "-", "*", "/"]
    expressions = []

    for i in range(4):
        expression = ""
        for j in range(3):
            num = random.choice(numbers)
            operator = random.choice(operators)
            expression += str(num) + operator
        expressions.append(expression)

    return "".join(expressions)