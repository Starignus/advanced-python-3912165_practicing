"""
Rerun the Unique Set of Punctation Characters in a Given String.

Task: 
Retunr the set of unique punctuation characters found in the given string.

Parameters"
the_str: A string to characters

Result:
result: The set of unique punctuation characters found in the string.

Constraints:
The the_str argument always contains a valid string.

Example 1:
Input: "the quick, brown fox: jumps over the lazy dog!Dog no ammused."
Result: {',', ':', '!', '.'}

Example 2:
Input: "Mary, Mary, quite contrary -- how_does_your garden grow??"
Result: {',', '-', '_', '?'}

"""

import string

def build_punctuation_set(the_str):
    """
    Getting the pictuation characters from the input string.
    Parameters:
    the_str: str
        Input string to search for punctuation characters.
    return: set
        The set of unique punctuation characters found in the string.
    """
    return set(punct for punct in the_str if punct in string.punctuation)

if __name__ == "__main__":
    # Example usage
    result = build_punctuation_set("the quick, brown fox: jumps over the lazy dog!Dog no ammused.")
    print(result)
    # Expected output: {',', ':', '!', '.'}

    result = build_punctuation_set("Mary, Mary, quite contrary -- how_does_your garden grow??")
    print(result)
    # Expected output: {',', '-', '_', '?'}