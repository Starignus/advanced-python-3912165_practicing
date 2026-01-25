# Example file for Advanced Python by Joe Marini
# Demonstrate how to use set comprehensions

# define a list of temperature data points
ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

# build a set of unique Fahrenheit temperatures



# List coprehension to convert Celsius to Fahrenheit
print("Unique Celsius temps:", set(ctemps))
temperatureF = [((9/5) * temp + 32) for temp in set(ctemps)]
print("Celsius temps:", ctemps)
print("Fahrenheit temps:", temperatureF)
# set comprehension to convert Celsius to Fahrenheit
temperatureFset = {((9/5) * temp + 32) for temp in ctemps}
print("Fahrenheit temps (from set comprehension to whole expresion):", temperatureFset)

# build a set from an input source
# count the unquie letters used in a string while converting to Upper case
# exclude the whitespaces and non-alpha characters
sTemp = "The quick brown fox jumped over the lazy dog"
uniqueLetters = {char.upper() for char in sTemp if not char.isspace()}
uniqueLetters_alpha = {char.upper() for char in sTemp if char.isalpha()}

print("Unique letters in string (not including spaces):", uniqueLetters)
print("Unique letters in string (alpha characters only):", uniqueLetters_alpha)