fruits = ["apple", "banana", "cherry", "peach", "watermelon"]

print(fruits.index("cherry"))

random_number = 0
print(f"{'Yes' if random_number == 1 else 'No'}")

speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and speed > 0 or acceleration > 0
print(is_moving)

def is_empty(string : str):
    empty = True
    for i in string:
        if i != ' ':
            empty = False
    return empty

print ("----")
print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True

print ("----")

def starts_with(string: str, start: str):
    if string.find(start) == 0:
        return True
    else:
        return False

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True

def greet(language:str):
    

print(greet('en'))         # Hi!
print(greet('fr'))         # Salut!
print(greet('pt'))         # Olá!
print(greet('de'))         # Hallo!
print(greet('sv'))         # Hej!
print(greet('af'))         # Haai!