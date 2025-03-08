import random

def get_random_python_code():
    """Generate a random Python code snippet."""
    # Define a list of operators
    operators = ["+", "-", "*", "/"]

    # Define a list of variables
    variables = ["x", "y", "z"]

    # Define a list of functions
    functions = ["sin", "cos", "tan"]

    # Combine the lists to create a random expression
    expression = "".join(random.choice(operators + variables + functions))

    return expression