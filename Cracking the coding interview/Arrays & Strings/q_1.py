'''
Problem: Is Unique
Description: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
Solved: True
'''

def is_unique(word):
    d = {}
    for c in word:
        if c in d:
            return 'Not unique!'
        d[c] = 0
    
    return 'Unique'

not_unique = 'jammer dit is niet uniek'
unique = 'uniek'

print(is_unique(not_unique))
print(is_unique(unique))