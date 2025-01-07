False or (True and False) # False
True or (1 + 2) # True
(1 + 2) or True # 3
True and (1 + 2) # 3
False and (1 + 2) # False
(1 + 2) and True # True
(32 * 4) >= 129  # False
False != (not True) # False
True == 4 # False
False == (847 == '847') # True

def even_or_odd(int):
    if int % 2 == 0:
        return 'even'
    else:
        return 'odd'

print(even_or_odd(15), even_or_odd(4))

# product 2, Product not found
"""
if foo():
    'bar'
else:
    qux()
"""

# Empty

def pseudo_upper(str):
    if len(str) >= 10:
        return str.upper()
    else:
        return str

print(pseudo_upper("Hello World"), pseudo_upper("goodbye"))