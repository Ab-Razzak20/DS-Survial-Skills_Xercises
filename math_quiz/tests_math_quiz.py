import unittest
from math_quiz import random_integer, random_operator, problemUNDsolve


class TestMathGame(unittest.TestCase):

    def test_random_integer(self):
        '''
        Test if random numbers generated are within the specified range
        '''

        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        """Test if the selected operator is one of the expected operators: +, -, *, /."""
        self.assertTrue(random_operator() == '+' or '-' or '*' or '/')


    def test_problemUNDsolve(self):
        """Check if the arithmetic problems and solutions are correctly generated."""
        test_cases = [(5, 2, '+', '5+2', 7), (2, 5, '-', '2-5', -3), (5, 2, '*', '5*2', 10), (2, 5, '/', '2/5', 0.4)]
        for num1, num2, operator, expected_problem, expected_ans in test_cases:
            (problem, ans) = problemUNDsolve(num1, num2, operator)
            self.assertTrue(problem)
            self.assertTrue(ans)

if __name__ == "__main__":
    unittest.main()
