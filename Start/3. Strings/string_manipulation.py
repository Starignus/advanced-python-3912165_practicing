# Example file for Advanced Python by Joe Marini
# Manipulating string content


test_str = "The quick, brown fox jumps over the lazy dog."

# upper, lower, title
print(test_str.upper())
print(test_str.lower())
print(test_str.title())

# strip, lstrip, rstrip
test_str2 = "   This string has whitespace   "

print("Original:", test_str2)
print("Stripped:", test_str2.strip())
print("Left stripped:", test_str2.lstrip())
print("Right stripped:", test_str2.rstrip())
# split creates a sequence from a single string

print("Split:", test_str.split(","))


# join concatenates an iterable into a single string
words = ["Hello", "world", "from", "Python"]
print(" ".join(words))
