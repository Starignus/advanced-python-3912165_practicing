# Example file for Advanced Python by Joe Marini
# Using special module names

import collections
# __name__ is the name of the module
# When run directly the value of the variable "__main__" which is a built-in name
# which tells us weather the code is being imported in another file or if the code
# is being executed as a program

print("Modele name", __name__)

# __file__ contains the path to the file from which the module was loaded
print("File name", __file__)

# __package__ indicates the package that the module belongs to.
print("Package name", __package__)
print(collections.__package__)

if __name__ == "__main__":
    print("This code is being run directly")