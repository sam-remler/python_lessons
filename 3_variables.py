"""
non-idiomatic
non-idiomatic
non-idiomatic
idiomatic
illegal
non-idiomatic
idiomatic
illegal
"""

"""
non-idiomatic
idiomatic
non-idiomatic
illegal
non-idiomatic
idiomatic
illegal
"""

name = 'Sam'
print(f"Good Morning, {name}")
print(f"Good Afternoon, {name}")
print(f"Good Evening, {name}")

age = 27

print(f"You are {age} years old")
print(f"In 10 years you will be {age + 10} years old")

# prints victor 3 times and nina 3 times

interest = 0.05
initial_investment = 1000
years_of_compounding = 5

balance = initial_investment * (1 + interest)**years_of_compounding
print(balance)

for _ in range(5):
    initial_investment *= (1+interest)
print(initial_investment)

"""
reassigns
nothing
reassigns
nothing
reassigns
mutates
mutates
mutates
nothing
reassigns
"""