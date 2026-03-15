import io
from contextlib import redirect_stdout
from helper import recurse_files
from unittest.mock import patch
import unittest
from path_walker import PathWalker

class TestHelper(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Runs ONCE before all tests in this class
        print("Setting up TestHelper class...")
        # fake file system structure for testing
        cls.fake_file_system = {
            "/root": ["file1.txt", "dirA"],
            "/root/dirA": ["file2.txt", "dirB"],
            "/root/dirA/dirB": ["file3.txt"]
        }
        cls.expected_output = (
            "- file1.txt\n"
            "dirA\n"
            "\t- file2.txt\n"
            "\tdirB\n"
            "\t\t- file3.txt\n"
        )


    def fake_listdir(self, path):
        # if path isn't in the dict, return an empty list
        return self.fake_file_system.get(path, [])
    
    def fake_isdir(self, path):
        return path in self.fake_file_system
    
    def fake_exists(self, path):
        return True


    @patch("helper.os.path.exists")
    @patch("helper.os.path.isdir")
    @patch("helper.os.listdir")
    def test_recurse_files(self, mock_listdir, mock_isdir, mock_exists):
        mock_listdir.side_effect = self.fake_listdir
        mock_isdir.side_effect = self.fake_isdir
        mock_exists.side_effect = self.fake_exists

        # Getting the output of the function
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            recurse_files("/root")
        output = buffer.getvalue()

        self.assertEqual(output, self.expected_output)


    @patch("helper.os.path.exists")
    @patch("helper.os.path.isdir")
    @patch("helper.os.listdir")
    @patch("path_walker.PathWalker.__str__")
    def test_recurse_files_with_pathwalker(self, mock_str, mock_listdir, 
        mock_isdir, mock_exists):

        # creating a dummy PathWalker
        pw = PathWalker(".")

        mock_listdir.side_effect = self.fake_listdir
        mock_isdir.side_effect = self.fake_isdir
        mock_exists.side_effect = self.fake_exists
        mock_str.return_value = "/root"

        # Getting the output of the function
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            recurse_files(pw)
        output = buffer.getvalue()

        self.assertEqual(output, self.expected_output)


if __name__ == "__main__":
    # Run all tests in this file (every method that starts with 'test')
    unittest.main()