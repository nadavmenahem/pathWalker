import unittest.mock
import os

class PathWalker:
    def __init__(self, dirPath):
        dirPath = os.path.expanduser(dirPath)  # expand '~' to home

        if not os.path.isdir(dirPath):
            raise NameError(f"path ({dirPath}) not found")

        self.dirPath = dirPath if os.path.isabs(dirPath) else \
                        os.path.join(os.getcwd(),dirPath)

    def __str__(self):
        return f"{self.dirPath}"
    
    def __repr__(self):
        return f"PathWalker('{self.dirPath}')"
    
    def __getitem__(self, subPath):
        return PathWalker(os.path.join(self.dirPath, subPath))