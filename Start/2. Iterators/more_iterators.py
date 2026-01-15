# Example file for Advanced Python by Joe Marini
import itertools

# define a list of days in English and French
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]


# for d in range(len(days)):
#     print(d + 1, days[d])

# the enumerate function retunrs a tuple with the index and the value of the collection

for idx, d in enumerate(days, start=1):
    print(idx, d)
# use zip to combine sequences. It stops when the shortest sequence is exhausted

for d in zip(days, daysFr):
    print(d)

# use enumerate and zip together
for idx, d in enumerate(zip(days, daysFr), start=1):
    print(idx, d[0], "=", d[1],"in French")

# use zip_longest (but using here the zip_longest from itertools)
seq1 = ["A","B","C","D","E","F"]
seq2 = [1, 2, 3, 4]
seq3 = "xyz"

result = itertools.zip_longest(seq1, seq2, seq3, fillvalue="-")
print("Result: ")
for item in result:
    print(item)