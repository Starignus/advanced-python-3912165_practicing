# Example file for Advanced Python by Joe Marini
# Demonstrate the use of documentation strings


def myFunction(arg1, arg2=None):
    """
    Docstring for myFunction
    
    :param arg1: Description
    :param arg2: Description
    """
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()
