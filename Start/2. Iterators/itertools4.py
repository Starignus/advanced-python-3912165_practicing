# Example file for Advanced Python by Joe Marini
# Itertools: combinations and permutations

import itertools


# product() produces the cartesian product of input iterables
cards = "A23456789TJQK"
suits = "SCHD"

deck = itertools.product(cards, suits)
# deck = list(deck)
# print(len(deck)," cards in the deck")  # 52 cards in a standard deck
# print("Deck of cards: ", deck)

# permutations() creates tuples of a given length with no repeated elements (oder matters AB != BA)
# The number of distinct types of items available is n, and the number of items to choose is r.
# Without replacement nPr = n! / (n-r)!; With replacement nPr = n^r
teams = ("A","B","C","D")
result = itertools.permutations(teams, 2)
# print("Permutations of teams: ")
print("Permutations of teams without replacement: ")
print(list(result))

# combinations() will create combinations of a given length with no repeats (oder does not matter AB == BA)
# Without replacement nCr = n! / r!(n-r)!; With replacement nCr = (n+r-1)! / r!(n-1)!
result = itertools.combinations(teams, 2)
print("Combinations of teams without replacement choosing 2: ")
print(list(result))

result = itertools.combinations(teams, 3)
print("Combinations of teams without replacement choosing 3: ")
print(list(result))

# combinations_with_replacement() will create combinations of a given length with repeats
result = itertools.combinations_with_replacement(teams, 2)
print("Combinations of teams with replacement choosing 2: ")
print(list(result))

# combinations_with_replacement() will create combinations of a given length with repeats
result = itertools.combinations_with_replacement(teams, 3)
print("Combinations of teams with replacement chosing 3: ")
print(list(result))