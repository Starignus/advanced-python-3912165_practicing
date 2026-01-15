# Example file for Advanced Python by Joe Marini
# Itertools: chain, chain.from_iterable

import itertools


# chain() creates a single iterable from multiple
x = itertools.chain("ABCDEFG",  "1234s")
print("Chained values: ", list(x))

# make a prepend function
def prepend(value, iterable):
    return itertools.chain([value], iterable)
print(list(prepend("a", "BCDEFG")))

# chain.from_iterable is an alternate usage of chain
s1 = "ABCDEFG"
s2 = [1,2,3,4,5]
s3 = ['$','%','@','&']

combined = itertools.chain.from_iterable([s1, s2, s3])
print("Combined values: ", list(combined))
