import unittest
from neural_nets import rectified_linear_unit, rectified_linear_unit_derivative
import numpy as np

class TestRectifiedLinearUnit(unittest.TestCase):
    def test_relu_positive(self):
        """Test ReLU with a positive input."""
        self.assertEqual(rectified_linear_unit(5), 5)

    def test_relu_zero(self):
        """Test ReLU with zero input."""
        self.assertEqual(rectified_linear_unit(0), 0)

    def test_relu_negative(self):
        """Test ReLU with a negative input."""
        self.assertEqual(rectified_linear_unit(-3), 0)

class TestRectifiedLinearUnitDerivative(unittest.TestCase):
    def test_relu_derivative_positive(self):
        """Test ReLU derivative with a positive input."""
        self.assertEqual(rectified_linear_unit_derivative(5), 1)

    def test_relu_derivative_zero(self):
        """Test ReLU derivative with zero input."""
        self.assertEqual(rectified_linear_unit_derivative(0),0)
        #self.assertTrue(np.isnan(rectified_linear_unit_derivative(0)))

    def test_relu_derivative_negative(self):
        """Test ReLU derivative with a negative input."""
        self.assertEqual(rectified_linear_unit_derivative(-3), 0)

if __name__ == '__main__':
    unittest.main()