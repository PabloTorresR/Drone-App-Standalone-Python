import unittest
from lib.utils import random_tuple_n_dimension, calculate_modulus_n_dimension


class TestUtilsFunctions(unittest.TestCase):
    def test_random_tuple_n_dimension(self):
        bounds = (10, 20, 30)
        result = random_tuple_n_dimension(*bounds)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 3)  # Check the number of dimensions
        for value, limit in zip(result, bounds):
            self.assertTrue(
                0 <= value <= limit
            )  # Check if values are within the specified range

    def test_calculate_modulus_n_dimension(self):
        vector = (3, 4, 5)
        result = calculate_modulus_n_dimension(vector)
        self.assertAlmostEqual(
            result, 7.0710678118654755, places=6
        )  # Check the modulus value with 6 decimal places
