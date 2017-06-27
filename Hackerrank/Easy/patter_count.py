'''
Problem: https://www.hackerrank.com/contests/w33/challenges/pattern-count/problem
Solved: True
'''

#!/bin/python3

import sys

def patternCount(s):
    count = 0
    start = False
    prev_ch = '0'
    
    for ch in s:
        if not start and ch == '1' and prev_ch != '1':
            start = True
        elif ch != '0' and ch != '1':
            start = False
        elif ch == '1' and start and not prev_ch == '1':
            count += 1
        
        prev_ch = ch
        
    return count

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = patternCount(s)
    print(result)
