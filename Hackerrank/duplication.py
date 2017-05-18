'''
Problem: https://www.hackerrank.com/contests/w32/challenges/duplication
Solved: True
'''

#!/bin/python3

import sys

def createString():
    s = [0]
    while len(s) < 1000:
        t = []
        for i in s:
            t.append(1-i)
        s.extend(t)
    return ''.join(str(x) for x in s)

def duplication(x, s):
    return s[x]

q = int(input().strip())
long_s = createString()
for a0 in range(q):
    x = int(input().strip())
    result = duplication(x, long_s)
    print(result)
