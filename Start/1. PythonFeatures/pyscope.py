# Example file for Advanced Python by Joe Marini
# Understanding Python scope


# declare a variable within the global scope
x=1

# define a local function with a variable "x"
def test():
    global x #bad practice use nonlocal instead
    x=10
    print("Inside function:", x)

# Run the test function and observe the two results
# test()
# print(x)

# x = x + 5
# print(x)

# Nested functions create inner scopes. These are called closures: Closure functions can capture and remember values from their enclosing scopes.
def multiplier_marker(factor):
    print("Creating a multiplier of", factor)
    def multiplyByFactor(number):
        print("Multiplying", number, "by", factor)
        return number * factor
    return multiplyByFactor

dobler = multiplier_marker(2)
tripler = multiplier_marker(3)
print(dobler(10))
print(dobler(15))
print(tripler(10))
print(tripler(15))