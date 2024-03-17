import os
import unittest
from app.io.input import read_from_file_builtin, read_from_file_pandas

data_folder = os.path.join(os.path.dirname(__file__), '..', '..', 'data')


class TestReadFromFile(unittest.TestCase):

    # Reading by builtin
    def test_read_from_file_builtin_empty(self):
        file_path = os.path.join(data_folder, 'empty_file.txt')
        with open(file_path, 'w'):
            pass
        self.assertEqual(read_from_file_builtin(file_path), '')

    def test_read_from_file_builtin_content(self):
        file_path = os.path.join(data_folder, 'test_file_builtin.txt')
        with open(file_path, 'w') as file:
            file.write('Test content')
        self.assertEqual(read_from_file_builtin(file_path), 'Test content')

    def test_read_from_file_builtin_nonexistent(self):
        with self.assertRaises(FileNotFoundError):
            read_from_file_builtin('nonexistent_file.txt')

    # Reading by pandas
    def test_read_from_file_pandas_empty(self):
        file_path = os.path.join(data_folder, 'empty_file_2.csv')
        with open(file_path, 'w'):
            pass
        self.assertEqual(read_from_file_pandas(file_path), None)

    def test_read_from_file_pandas_csv(self):
        file_path = os.path.join(data_folder, 'test_file_pandas.txt')
        with open(file_path, 'w') as file:
            file.write('Test content')
        self.assertEqual(read_from_file_pandas(file_path), 'Test content')

    def test_read_from_file_pandas_nonexistent(self):
        with self.assertRaises(FileNotFoundError):
            read_from_file_pandas('nonexistent_file_2.txt')


if __name__ == '__main__':
    unittest.main()
