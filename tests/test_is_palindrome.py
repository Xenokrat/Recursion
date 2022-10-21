import unittest

from is_palindrome_recr import is_palindrome_recr


class MyTestCase(unittest.TestCase):
    def test_is_palindrome(self):
        palindrome = 'Madam'
        not_palindrome = 'sometesttext'
        self.assertTrue(is_palindrome_recr(palindrome))

        palindrome = 'Lallal'
        self.assertTrue(is_palindrome_recr(palindrome))

        self.assertFalse(is_palindrome_recr(not_palindrome))

if __name__ == '__main__':
    unittest.main()
