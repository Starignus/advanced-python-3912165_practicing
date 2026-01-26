# Example file for Advanced Python by Joe Marini
# Understanding the built-in exception classes in Python

# IndexError occurs when you try to access an index that is out of range
int_list = [0,3,6,1,8,7,3,5]
# print(int_list[10])  # This will raise an IndexError
# print(int_list["A"])  # This will raise a TypeError

# KeyError is similar - it is raised when a key is not found in a Dictionary
my_dict = {1: "one", 2: "two", 3: "three"}
# print(my_dict[4])  # This will raise a KeyError

# FileNotFoundError is raised when you try to access a file that doesn't exist
# with open("non_existent_file.txt", "r") as f:
#   print(f.read())  # This will raise a FileNotFoundError


# FileExistsError is raised when a file or directory already exists
import os
# current working directory path
dir_path = os.path.dirname(os.path.realpath(__file__))
# os.mkdir(os.path.join(dir_path, "testdir")) # This will raise a FileExistsError


# NotADirectoryError is raised when try to perform a dir operation on a non-dir object
os.listdir(os.path.join(dir_path, "myfile.txt"))  # This will raise a NotADirectoryError