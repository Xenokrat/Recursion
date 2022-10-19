import unittest

from recursive_power import calc_recursive_power


class TestRecursivePower(unittest.TestCase):
    def test_recursive_power(self) -> None:
        self.assertEqual(calc_recursive_power(5, 3), 125)
        self.assertEqual(calc_recursive_power(2, 8), 256)
