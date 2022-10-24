import unittest

from find_all_files import find_all_files


class MyTestCase(unittest.TestCase):
    def test_find_all_files(self) -> None:
        files = find_all_files(r'C:\Users\Mantis\test_delete')
        self.assertListEqual(
            files, [
                'test.txt',
                'test2.txt',
                'another_one.txt',
                'kek.txt',
                'and_another_one.txt'
            ]
        )



if __name__ == '__main__':
    unittest.main()
