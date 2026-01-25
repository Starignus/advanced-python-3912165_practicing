# Example file for Advanced Python by Joe Marini
# Sequences and slicing

from collections import deque

names = ["Jim", "Pam", "Creed", "Michael", "Dwight", "Oscar", "Kevin", "Phyllis"]

# a slice is a subset of a sequence. The form is [start:stop:step]
print(names[1:4])  # from index 2 to (but not including) index 5

# using a step 
print(names[:7:2])  # every second name up to index 7

# shorthand
print(names[:3])  # from beginning to index 3
print(names[5:])  # from index 5 to the end


# reversing with step of -1
print(names[::-1])  # reverse the entire list
# assigning sequences
newnames = ["Anady", "Stanley", "Ryan"]
names[2:4] = newnames  # replaces index 2 and 3 with new names
print(names)
# the del operator works with slices
del names[0:2]  # deletes the first two items
print(names)

# not all sequence types support slicing, like the deque data structure
# from the collection module.
# A deque is a double-ended queue that is optimised for adding and removing elements from either end
deque_names = deque(["Jim", "Pam", "Creed", "Michael", "Dwight", "Oscar", "Kevin", "Phyllis"])

for name in deque_names:
  print(name, "", end="")
print()
print(len(deque_names))
# slicing is not supported
# print(deque_names[1:4])  # this would raise an error