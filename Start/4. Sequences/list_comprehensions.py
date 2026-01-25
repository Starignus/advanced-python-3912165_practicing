# Example file for Advanced Python by Joe Marini
# Demonstrate how to use list comprehensions


# define two lists of numbers
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Perform a mapping and filter function on a list using built-in functions

eventSquared = list(map(lambda x: x**2, evens))
print("Evens squared:", eventSquared)

# Add filter for values grater than 4 and less than 16

eventSquared = list(map(lambda x: x**2, filter(lambda x: x > 4 and x < 16, evens)))
print("Evens squared greater than 4 and less than 16:", eventSquared)

# Now do the same thing with list comprehensions
# Derive a new list of numbers frm a given list
print("Evens squared:", [x**2 for x in evens])

evenSquared = [x**2 for x in evens if x > 4 and x < 16]
print("Evens squared greater than 4 and less than 16:", evenSquared)

# Limit the items operated on with a predicate condition
oddSquared = [x**2 for x in odds if x > 3 and x < 17]
print("Odds squared greater than 3 and less than 17:", oddSquared)