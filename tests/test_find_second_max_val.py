import unittest

from find_second_max_val import find_second_max_val


class TestFindSecondMax(unittest.TestCase):
    def test_find_second_max(self) -> None:
        example1 = [1, 2, 3, 4, 5, 6, 7, 8]
        example2 = [1, 2, 3, 4, 5, 6, 8, 8]
        example3 = [1]
        self.assertEqual(find_second_max_val(example1), 7)
        self.assertEqual(find_second_max_val(example2), 8)
        self.assertIsNone(find_second_max_val(example3))
        self.assertEqual(len(example1), 8)
        self.assertEqual(len(example2), 8)
