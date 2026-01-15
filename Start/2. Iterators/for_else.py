# Example file for Advanced Python by Joe Marini
# The for-else loop construct

names = ["Jim", "Pam", "Creed", "Michael", "Dwight", "Oscar", "Kevin", "Phyllis"]

# The else clause on a for loop is only executed if the loop completes every iteration
# def findname(target):
#     for name in names:
#         if name == target:
#             print("Name found");
#             return True
    
#     print("Name not found")
#     return False

# print(findname("Creed"))
# print(findname("Tom"))

def findname(target):
    for name in names:
        if name == target:
            print("Name found");
            return True
    else:
        print("Name not found")
        return False

print(findname("Creed"))
print(findname("Tom"))

# Check if a number is prime

def is_prime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} is not a prime number")
            return False
    else:
        print(f"{n} is a prime number")
        return True

is_prime(31)
is_prime(56)