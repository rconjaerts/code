'''
Problem: One Way
Description: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
Solved: True
'''

def check_insert_delete(long, short):
    j = 0
    status = True

    for i in range(len(short)):
        if long[i] != short[j] and status:
            status = False
        elif long[i] != short[j] and not status:
            return False
        else:
            j += 1

    return not status if long[-1] == short[-1] else status

def check_replace(s1, s2):
    status = True

    for i in range(len(s1)):
        if s1[i] != s2[i] and status:
            status = False
        elif s1[i] != s2[i] and not status:
            return False

    return True

string1 = 'pales'
string2 = 'paleo'

if len(string1) > len(string2) and len(string1)-len(string2) == 1:
    print(check_insert_delete(string1, string2))
elif len(string1) < len(string2) and len(string2)-len(string1) == 1:
    print(check_insert_delete(string2, string1))
elif len(string1) == len(string2):
    print(check_replace(string1, string2))
else:
    print('False')