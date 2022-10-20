import unittest

from list_len_recr import get_list_length


class MyTestCase(unittest.TestCase):
    def test_get_list_len_recr(self):
        list_ = ['a', 'b', 'c', 'd', 1, 2]
        self.assertEqual(len(list_), get_list_length(list_))


if __name__ == '__main__':
    unittest.main()
