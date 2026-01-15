"""
Quiz on itertools

You get multeple set of list that contains integer numbers. 
Your task is to return the max value from all the individual lists using itertools module.

Paranmeters: 

numbers: List of List of integers

Result:
int: The largest number in all the lists

Cosntraints: All the input values will be valid integers.

Example: [[2,3,20], [30, 56], [8, 4, 28, 31]]]
Returns: 56

Hint: Refer to the list of built-in functions for Python, as well as the interools module.
"""

import itertools

# show_expected_result = False
# show_hints = False

def find_largest(numbers):
    # write your code here
    merged = itertools.chain.from_iterable(numbers)
    return max(merged)

if __name__ == "__main__":
    numbers = [
    [43, 2, 77, 48, 24, 9, 3, 65, 41, 42, 10, 75, 14, 69, 61],
    [20, 47, 69, 38, 2, 49, 76, 42, 81, 34, 10, 47, 76, 85, 81, 72],
    [92, 46, 25, 61, 75, 40, 87, 9, 52, 77, 0, 11, 25],
    [48, 74, 81, 71, 32, 82, 39, 74, 37, 72, 15],
    [8, 26, 12, 71, 5, 83, 75, 30, 34, 77]
]
result = find_largest(numbers)
print("The largest number is: ", result)