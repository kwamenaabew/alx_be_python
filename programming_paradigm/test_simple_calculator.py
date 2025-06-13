import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Create a calculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        # Positive integers
        self.assertEqual(self.calc.add(2, 3), 5)
        # Negative and positive
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Floats
        self.assertAlmostEqual(self.calc.add(2.5, 3.1), 5.6)
        # Zero
        self.assertEqual(self.calc.add(0, 5), 5)

    def test_subtraction(self):
        # Positive result
        self.assertEqual(self.calc.subtract(5, 3), 2)
        # Negative result
        self.assertEqual(self.calc.subtract(3, 5), -2)
        # With zero
        self.assertEqual(self.calc.subtract(0, 5), -5)
        # Floats
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)

    def test_multiplication(self):
        # Positive integers
        self.assertEqual(self.calc.multiply(4, 5), 20)
        # Multiplication by zero
        self.assertEqual(self.calc.multiply(4, 0), 0)
        # Negative numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        # Floats
        self.assertAlmostEqual(self.calc.multiply(2.5, 4.0), 10.0)

    def test_division_normal(self):
        # Integer division
        self.assertEqual(self.calc.divide(10, 2), 5)
        # Float result
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)
        # Division resulting in float
        self.assertAlmostEqual(self.calc.divide(5.5, 2.2), 2.5)

    def test_division_by_zero(self):
        # Should return None when divisor is zero
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    def test_divide_negative(self):
        # Negative numerator
        self.assertEqual(self.calc.divide(-10, 2), -5)
        # Negative denominator
        self.assertEqual(self.calc.divide(10, -2), -5)
        # Both negative
        self.assertEqual(self.calc.divide(-10, -2), 5)

if __name__ == '__main__':
    unittest.main()
