import unittest
from unittest.mock import patch
import io

from print_even_numbers import print_even_numbers


class MyTestCase(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_even_numbers(self, mock_stdout) -> None:
        print_even_numbers([
            1, 2, 4, 7, 18, 21, 0
        ])
        self.assertEqual(mock_stdout.getvalue(), '2 4 18 0 ')


if __name__ == '__main__':
    unittest.main()
