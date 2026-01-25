# Example file for Advanced Python by Joe Marini
# Sequence comparisons

import itertools


# define some lists
seq1 = [1, 2, 3, 6, 10, 15, 34, 56]
seq2 = [1, 2, 5, 7, 9, 18, 22, 38, 91]

# define a tuple
seq3 = (1, 2, 3, 6, 10, 15, 34, 56)

# compare the sequences
# Python uses the first differing element to determine the outcome of the comparison

print("seq1 == seq2:", seq1 == seq2) # False
print("seq1 != seq2:", seq1 != seq2) # True
print("seq1 < seq2:", seq1 < seq2) # True Because the 3rd value 3 is less than 5
print("seq1 <= seq2:", seq1 <= seq2) # True
print("seq1 > seq2:", seq1 > seq2) # False Because  the 3rd value 3 is less than 5
print("seq1 >= seq2:", seq1 >= seq2) # False
print()
# sequences that have equal values but different number of items:
# When the sequences are of different lengths, and all items are equal up to the length of the shorter sequence,
# the longer sequence is considered greater than the shorter one.

seq4 = [10, 20, 30]
seq5 = [10, 20, 30, 40, 50]

print("seq4 > seq5:", seq5 > seq4) # True Because seq5 is longer than seq4
print("seq4 < seq5:", seq5 < seq4) # False Because seq5 is longer than seq4
print()

# Sequences must be of the same type to be compared
print("seq1 == seq3:", seq1 == seq3) # False because we can't compare list with tuple
print("seq1 != seq3:", tuple(seq1) == seq3) # True but this can be problematic fromthe perfomrace point of view
# We can use the intertools module to compare sequences of different types

# use the all() function to compare two arbitrary sequences that is more mermory efficient
result = all(a == b for a, b in itertools.zip_longest(seq1, seq3))
print("seq1 == seq3:", result) # True

print()