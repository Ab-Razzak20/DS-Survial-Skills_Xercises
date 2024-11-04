import random


def random_integer(min, max):
    """
    generate a random integer in the range of the given numbers.
    """
    return random.randint(min, max)


def random_operator():
    """
    randomly select an arithmetic operator to perform certain mathematical operations.
    """
    return random.choice(['+', '-', '*', '/'])


def problemUNDsolve(num1, num2, operator):
    """
    perform some mathematical operations on two numbers and return the problem in string format and the result.
    """
    prob = f"{num1} {operator} {num2}"
    if operator == '+':
        ans = num1 + num2            # fixed the bug for incorrect arithmetic operation
    elif operator == '-':
        ans = num1 - num2            # fixed the bug for incorrect arithmetic operation
    elif operator == '/':
        ans = num1 / num2
    else:
        ans = num1 * num2            # operator == '*'
    return prob, ans

def math_quiz():
    """Main function to run the Math Quiz Game."""
    score = 0
    ques = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(3):                          # Fixed the bug:  'float' object cannot be interpreted as an integer
        n1 = random_integer(1, 10);
        n2 = random_integer(1, 5);    # Fixed the bug: `5.5` is not a valid integer
        o = random_operator()

        PROBLEM, ANSWER = problemUNDsolve(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        try:
            useranswer = int(input("Your answer: "))
        except ValueError:
            print("Invalid! Please enter a number.. ")

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")



    print(f"\nGame over! Your score is: {score}/{ques}")





if __name__ == "__main__":
    math_quiz()
