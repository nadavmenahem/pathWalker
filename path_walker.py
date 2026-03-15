# import unittest.mock
import os

class PathWalker:
    """A class to represent a directory path and allow for easy navigation and 
    iteration through its contents."""

    def __init__(self, dirPath):
        assert isinstance(dirPath, str), f"dirPath must be a string, got {type(dirPath)}"

        dirPath = os.path.expanduser(dirPath) # expand '~' to home
        dirPath = os.path.abspath(dirPath)    # converts to an absolute path and resolves . and ..
        self.dirPath = dirPath

        if not os.path.isdir(dirPath):
            raise NameError(f"path ({dirPath}) not found")

    def __str__(self):
        return f"{self.dirPath}"
    
    def __repr__(self):
        return f"PathWalker('{self.dirPath}')"
    
    def __getitem__(self, subPath):
        os.path.normpath(subPath)
        return PathWalker(os.path.join(self.dirPath, subPath))
    
    def __iter__(self):
        files = os.listdir(self.dirPath)
        self.filesIter = iter(files)
        return self

    def __next__(self):
        return next(self.filesIter)