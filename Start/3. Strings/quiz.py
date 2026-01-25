"""
Extracting Information about Strings Quiz 

You're given a string and a term to search the string for.

Your task: Return a dictionary that contains information about the string.

Parameters
the_str: A string
search_term: A term to search the string for

Result
dict: A dictionary that contains information about the string. The dictionary will have the following format:

{

"Punctuation": (int),
"Whitespace": (int),
"Uppercase": (int),
"Lowercase": (int),
"Found": (bool),
"Index": (int)

}
	• "Punctuation" is the number of punctuation characters.
	• "Whitespace" is the number of whitespace characters.
	• "Uppercase" is the number of uppercase characters.
	• "Lowercase" is the number of lowercase characters.
	• "Found" indicates whether the search_term was found, regardless of case.
	• "Index" is the index where the term was found, or -1 if not found. If there is more than one instance of the search term, return the index of the first occurrence starting from the beginning of the string.

    
    Some documentation that may help you:
    https://docs.python.org/3/library/stdtypes.html#string-methods
    https://docs.python.org/3/library/string.html#grammar-token-format-string-index_string
    
"""

import string



def process_string(the_str, search_term):
    """"
    Returns a dictionary with information about the string

    the_str: str
    search_term: str
    return: dict
    """
    punctuation_count =sum(1 for punct in the_str if punct in string.punctuation)
    whitespace_count = sum(1 for space in the_str if space in string.whitespace)
    uppercase_count = sum(1 for upper in the_str if upper.isupper())
    lowercase_count = sum(1 for lower in the_str if lower.islower())
    # I prefer this way of checking for existence instead of using find() method
    if search_term.lower() in the_str.lower(): 
        found = True
        # Find the index of the first occurrence, case insensitive
        index = the_str.lower().index(search_term.lower())
    else:
        found = False
        index = -1  

    return {
        "Punctuation": punctuation_count,
        "Whitespace": whitespace_count,
        "Uppercase": uppercase_count,
        "Lowercase": lowercase_count,
        "Found": found,
        "Index": index
    }



if __name__ == "__main__":
    # Example usage
    result = process_string("Hello, World! Test is a Test with lost of test.", "test")
    print(result)
    # Expected output:
    # {
    # "Punctuation": 3,
    # "Whitespace": 9,
    # "Uppercase": 4,
    # "Lowercase":  31,
    # "Found": True,
    # "Index": 14
    # }
    result = process_string("The quick, brown 'fox' jumps OVER the lazy dog; dog not impressed!", "Fox")
    print(result)
    # Expected output:
    # {
    # Punctuation': 5, 
    # 'Whitespace': 11, '
    # Uppercase': 5, 
    # 'Lowercase': 45, 
    # 'Found': True, 
    # 'Index': 18
    #}
    result = process_string("This, is a TEST string!", "Toast")
    print(result)
    # Expected output:
    # {
    # 'Punctuation': 2, 
    # 'Whitespace': 4, 
    # 'Uppercase': 5, 
    # 'Lowercase': 12, 
    # 'Found': False, 
    # 'Index': -1
    #}
