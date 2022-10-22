import unittest
from unittest.mock import patch
import io

from print_even_indexes import print_even_indexes


class MyTestCase(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_even_numbers(self, mock_stdout) -> None:
        print_even_indexes([
            1, 'kek', 'kek2', 3, (1, 2, 3)
        ])
        self.assertEqual(mock_stdout.getvalue(), '1 kek2 (1, 2, 3) ')


if __name__ == '__main__':
    unittest.main()
