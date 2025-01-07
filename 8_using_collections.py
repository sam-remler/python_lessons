print(list(range(0,25,3))[6])

name = 'Launch School'
num = name.find('c')
print(name[num: num + 6])

original = (1, 2, 3, 4, 5)
new = list(original)
new.pop()
new.sort(reverse=True)
new.pop()
print(tuple(new))

pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}
print(pets['Dog'])
print(pets.get('Lizard'))
print(pets.get('Lizard', '<silence>'))

'cat' # yes
(3, 1, 4, 1, 5, 9, 2) # yes
['a', 'b'] # no
{'a': 1, 'b': 2} # no
range(5) # yes, but not advised?
{1, 4, 9, 16, 25} # no
3 # yes
0.0 # yes
frozenset({1, 4, 9, 16, 25}) # yes

print('abc-def'.isalpha())
print('abc_def'.isalpha())
print('abc def'.isalpha())
print('abc def'.isalpha() and
      'abc def'.isspace())
print('abc def'.isalpha() or
      'abc def'.isspace())
print('abcdef'.isalpha())
print('31415'.isdigit())
print('-31415'.isdigit())
print('31_415'.isdigit())
print('3.1415'.isdigit())
print(''.isspace())

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
info.replace(':','+')

stuff = [
    ['hello', 'world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]

stuff[1][3] = 606

print(stuff)

cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            },
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            },
        },
    },
}

print(cats['Cocoa'])