# Example file for Advanced Python by Joe Marini
# Working with basic exception handling

# Try to execute some code that might cause an exception:

# Original code
# num = input("Enter the first number: ")
# denom = input("Enter the second numnber: ")
# n = int(num)
# d = int(denom)
# print(n/d)


# Updated code with exception handling
try:
  num = input("Enter the first number: ")
  denom = input("Enter the second numnber: ")
  n = int(num)
  d = int(denom)
  results = n/d
except ZeroDivisionError as e:
  print("You can't divide by zero!", e)
except ValueError as e:
  print("You must enter numeric values only!", e)
else:
  print("Division performed successfully!", results)
finally:  
  print("Exiting the program. Goodbye!")
