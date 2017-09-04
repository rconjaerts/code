'''
Problem: URLify
Description: Write a method to replace all spaces in a string with '%20: You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string.
Solved: True
'''

# custom function
def replace_spaces_custom(string):
    return ''.join(['%20' if x == ' ' else x for x in string])

# build in function
def replace_spaces(string):
    return string.replace(' ', '%20')

test1 = 'I shall be urlified'
print(replace_spaces_custom(test1))