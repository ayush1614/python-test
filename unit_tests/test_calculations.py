import unittest
from services.calculations import Calculations

class TestCalculations(unittest.TestCase):

    def setUp(self):
        self.Calculations = Calculations()

    def test_add(self):
        output = self.Calculations.add(5,2)
        expected = 7
        self.assertEqual(expected,output)
    def test_minuse(self):
        output = self.Calculations.minus(5, 2)
        expected = 3
        self.assertEqual(expected,output)
    def test_multiply(self):
        output = self.Calculations.multiply(5,2)
        expected = 10
        self.assertEqual(expected,output)
    def test_division(self):
        output = self.Calculations.division(6,2)
        expected = 3
        self.assertEqual(expected,output)

