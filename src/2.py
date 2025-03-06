import random
def generate_math_problem(difficulty):
    if difficulty == "easy":
        problem = f"{random.randint(1, 10)} x {random.randint(1, 10)} = ?"
    elif difficulty == "medium":
        problem = f"({random.randint(1, 20)} + {random.randint(1, 20)}) x {random.randint(1, 20)} - {random.randint(1, 20)} = ?"
    elif difficulty == "hard":
        problem = f"{random.choice(['sin', 'cos', 'tan'])}({random.randint(1, 360)}) x {random.randint(1, 100)} - {random.randint(1, 100)} = ?"
    return problem
