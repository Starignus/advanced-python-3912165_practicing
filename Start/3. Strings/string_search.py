# Example file for Advanced Python by Joe Marini


sample_text = "The quick brown fox jumps over the lazy dog."

# Using find() to find the first occurrence of a substring

print("First occurance of 'the':", sample_text.lower().find("the"))


# Example with optional start and end parameters

print("First occurance of 'the':", sample_text.lower().find("the", 5, 35))

# Using index() to find the first occurrence of a substring (raises ValueError if not found)
try:
  print("First occurance of 'the':", sample_text.lower().index("fax"))
except ValueError as e:
  print("ValueError:", e)

# The 'in' operator can be used for Boolean testing:
print("'fox' found?", 'fox' in sample_text.lower())
# Using rfind() to find the last occurrence of a substring
print("Last occurance of 'the':", sample_text.lower().rfind("the"))

# Using rindex() to find the last occurrence of a substring (raises ValueError if not found)
print("Last occurance of 'jump':", sample_text.lower().rindex("jump"))

# The replace() function will find content in the string and replace it
print("original string:", sample_text)
print("replaced string:", sample_text.replace("fox", "cat")) 

# The strings are inmutable, so the original string is unchanged