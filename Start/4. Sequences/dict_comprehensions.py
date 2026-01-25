# Example file for Advanced Python by Joe Marini
# Demonstrate how to use dictionary comprehensions

# define a list of temperature values
ctemps = [0, 12, 34, 100]

# Use a comprehension to build a dictionary

tempDict = {temp: (9/5) * temp + 32 for temp in ctemps if temp < 100}
print("Celsius to Fahrenheit Dictionary (temp < 100):", tempDict)
print("Celsius temps 12:", tempDict[12])
print()
# Merge two dictionaries with a comprehension
team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
team2 = {"White": 12, "Macke": 88, "Perce": 4}

# Create a combined dictionary of players 
# {k:v for team in (team1, team2) for k,v in team.items()}}
# The first expresion gives me the team in the (team1, team2) tuple
# The second expresion iterates over each team's items
# The if condition filters players aged 18 and older

team_result= {player: age for team in (team1, team2) for player, age in team.items()}
team_result_18 = {player: age for team in (team1, team2) for player, age in team.items() if age >= 18}
print("Combined team dictionary:", team_result)
print("Combined team dictionary (age >= 18):", team_result_18)