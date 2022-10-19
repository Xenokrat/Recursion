import unittest

from recurcive_sum_of_digits import calc_recr_sum_of_digits


class MyTestCase(unittest.TestCase):
    def test_recr_sum_of_digits(self) -> None:
        self.assertEqual(calc_recr_sum_of_digits(12345), 15)
        self.assertEqual(calc_recr_sum_of_digits(1), 1)
        self.assertEqual(calc_recr_sum_of_digits(10000000001), 2)


if __name__ == '__main__':
    unittest.main()
