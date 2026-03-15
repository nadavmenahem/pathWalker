import os

from path_walker import PathWalker
from unittest.mock import patch
import unittest


class TestPathWalker(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Runs ONCE before all tests in this class
        print("Setting up TestPathWalker class...")
        cls.pw =  PathWalker(".")
        cls.pw2 = PathWalker("..")
        cls.pw3 = PathWalker("~")
        cls.pw4 = PathWalker("/mnt/c/Users/nadav/work/exercises/path-walker/nothing")
        cls.cwd = os.getcwd()
        cls.parentDir = os.path.dirname(cls.cwd)


    # def setUp(self):
    #     print("Setting up TestPathWalker class...")
        

    def test_init(self):
        # Non-existent path should raise an error
        with self.assertRaises(NameError) as context:
            PathWalker("nonexistent")
        expected_msg = f"path ({os.path.join(self.cwd, 'nonexistent')}) not found"
        self.assertEqual(expected_msg, str(context.exception))

        # Non-string input should fail the assertion
        with self.assertRaises(AssertionError) as context:
            PathWalker(3)
        expected_msg = f"dirPath must be a string, got {type(3)}"
        self.assertEqual(expected_msg, str(context.exception))

        self.assertEqual(str(self.pw), self.cwd)


    def test_str(self):
        self.assertEqual(str(self.pw), self.cwd)
        self.assertEqual(str(self.pw2), self.parentDir)
        self.assertEqual(str(self.pw3), "/root")
        self.assertEqual(str(self.pw4), "/mnt/c/Users/nadav/work/exercises/" \
            "path-walker/nothing")
        

    def test_repr(self):
        self.assertEqual(repr(self.pw), f"PathWalker('{self.cwd}')")
        self.assertEqual(repr(self.pw2), f"PathWalker('{self.parentDir}')")
        self.assertEqual(repr(self.pw3), f"PathWalker('/root')")
        self.assertEqual(repr(self.pw4), f"PathWalker('/mnt" \
            "/c/Users/nadav/work/exercises/path-walker/nothing')")
        

    def test_iter(self):
        # Mock directory contents
        with patch('path_walker.os.listdir') as mock_listdir:
            mocked_files = ['file1.txt', 'file2.csv', 'subfolder']
            mock_listdir.return_value = mocked_files

            for subwalker, name in zip(self.pw, mocked_files):
                self.assertEqual(str(subwalker), name)


    @patch("path_walker.os.path.isdir", return_value=True)
    def test_getitem(self, mock_isdir):
        with patch('path_walker.os.path.join') as mock_join:
            mock_join.return_value = str(self.pw) + "/subfolder"
            subwalker = self.pw["subfolder"]
            self.assertEqual(str(subwalker), str(self.pw) + "/subfolder")

            print(f'subwalker: {str(subwalker)}')
    

if __name__ == "__main__":
    # Run all tests in this file (every method that starts with 'test')
    unittest.main()