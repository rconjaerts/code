'''
Problem: Check Permutation
Description: Given two strings, write a method to decide if one is a permutation of the other.
Solved: True
'''

def is_permutation(word1, word2):
    d = {}

    for c in word1:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    for c in word2:
        if c not in d:
            return 'Not a permutation'
        else:
            d[c] -= 1

    for k, v in d.iteritems():
        if v != 0:
            return 'Not a permutation'

    return 'Permutation!'

perm1 = 'bones'
perm2 = 'snoeb'
not_perm1 = 'classic'
not_perm2 = 'rock'

print(is_permutation(perm1, perm2))
print(is_permutation(not_perm1, not_perm2))