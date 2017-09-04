'''
Problem: Palindrome Permutation
Description: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
Solved: True
'''

def is_palin_perm(string):
    string = string.replace(' ', '')

    d = {}
    for c in string:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    
    uneven = False
    for k, v in d.iteritems():
        if v%2 != 0 and uneven:
            return 'Not possible'
        if v%2 != 0:
            uneven = True

    return 'Possible'

pos = 'tact coa'
not_pos = 'aassddfffg'

print(is_palin_perm(pos))
print(is_palin_perm(not_pos))