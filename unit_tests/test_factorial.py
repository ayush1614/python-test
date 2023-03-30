import unittest
from services.factorial import Factorial

class TestFactorial(unittest.TestCase):
    def setUp(self):
        self.Factorial = Factorial()

    def test_factorial(self):
        self.assertEqual(120, self.Factorial.factorial(5))