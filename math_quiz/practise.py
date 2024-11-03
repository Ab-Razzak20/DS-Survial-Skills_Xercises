import random
x = random.randint(1, 100)
z = random.randint(1, 100)
y = random.choice(['+', '-', '*', '/'])
def funk(m, n, o):
    if o=='+':
        res = m+n
    elif o == '-':
        res = m - n
    elif o=='*':
        res = m*n
    else:
        res = m/n
    return f'{m}{o}{n}', res

points = 0
pi = 4
for i in range(pi):
    problem, answer = funk(x, z, y)
    print(f"\nQues: {problem}")
    userans = int(input("Ihr ans: "))

    if userans == answer:
        print("Bravo!")
        points += 1
    else:
        print("So sorry!")

print(f'final point: {points}')

import unitest
from math_quiz import function_A, function_B, function_C

class TestMathGame(unittest, testcase):
    def test_funkA(self):
        for _ in range(1000):
            self.assertTrue(1<=function_A(1, 10)<=10)

if __nmae__ == '__main__':
    unitest.main()

# print(problem, answer)
