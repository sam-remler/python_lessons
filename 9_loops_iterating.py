# Because counter isnt incremented


current_age = 27
for delta_age in range(10, 40, 10):
    print(f"You will be {current_age + delta_age} in {delta_age} years")

print("-----\n")
my_list = [6, 3, 0, 11, 20, 4, 17]

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
print("-----\n")
for i in my_list:
    print(i)
print("-----\n")
i = 0
while i < len(my_list):
    if i % 2 == 0:
        print(my_list[i])
    i += 1
print("-----\n")
for i in my_list:
    if i % 2 == 1:
        print(i)
print("-----\n")
my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]
print("-----\n")
for i in my_list:
    for j in i:
        if j % 2 == 0:
            print(j)
print("-----\n")

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

new_list = []
for i in my_list:
    if i % 2 == 0:
        new_list.append('even')
    else:
        new_list.append('odd')

print(new_list)

print("-----\n")

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

def find_integers(l):
    new_list = []
    for i in l:
        if type(i) is int:
            new_list.append(i)
    
    return new_list

integers = find_integers(my_tuple)
print(integers)  

print("-----\n")

my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

new_dict = {key : len(key) for key in my_set if len(key) % 2 != 0 }

print(new_dict)

print("-----\n")

def for_factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

def while_factorial(n):
    result = 1
    i = 1
    while i < n+1:
        result *= i
        i += 1
    return result

print(for_factorial(5))
print(while_factorial(5))

print("-----\n")

import random

highest = 10
while True:
    number = random.randrange(highest + 1)
    if number == highest: 
        break
    print(number)

print("-----\n")

my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

index1 = 0
index2 = 0

outer_index = 0
while outer_index < len(my_list):
    inner_index = 0
    while inner_index < len(my_list[outer_index]):
        number = my_list[outer_index][inner_index]
        if number % 2 == 0:
            print(number)

        inner_index += 1

    outer_index += 1

print("-----\n")

