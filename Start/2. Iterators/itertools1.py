# Example file for Advanced Python by Joe Marini
# Itertools: count, cycle, accumulate


import itertools

names = ["Joe", "Jane", "Jim"]

# cycle iterator can be used to cycle over a collection infinitely

# cycker = itertools.cycle(names)
# print(type(cycker))
# print(next(cycker))
# print(next(cycker))
# print(next(cycker))
# print(next(cycker))

# use count to create a simple counter

# counter = itertools.count(start=100, step=10)
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# accumulate creates an iterator that accumulates values
vals = [10,20,30,40,50,40,30]

accum = itertools.accumulate(vals, max)
# print(list(accum))

# amortize a loan over a set number of payments for a 2000 loan at 4%
payments = [100, 125, 200, 105, 100, 120, 110, 130, 150, 100, 110, 120]

updated = lambda balance, payment: round(balance * 1.04) - payment 
balance = itertools.accumulate(payments, updated, initial=2000)
print(list(balance))