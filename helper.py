import os
from path_walker import PathWalker

def recurse_files(path, depth=0):
    """
    Recursively walk through the directory and print all files and directories.
    """
    # if path is a PathWalker instance, convert it to string
    if isinstance(path, PathWalker): 
        path = str(path)

    path = os.path.expanduser(path) # expand '~' to home

    # Check if path exists
    if not os.path.exists(path): # checks relative and absolute paths
        print(f"Path does not exist: {path}")
        return
    
    for name in os.listdir(path):
        sub_path = os.path.join(path, name)
        
        if os.path.isdir(sub_path): # sub path is a directory
            print("\t" * depth + f"{os.path.basename(sub_path)}")
            recurse_files(sub_path, depth+1) # RECURSIVE call to walk through the directory

        else: # sub path is a file
            print("\t" * depth + f"- {os.path.basename(sub_path)}") 