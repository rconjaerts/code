'''
Problem: https://www.hackerrank.com/contests/w32/challenges/fight-the-monsters
Solved: True
'''

#!/bin/python3

import sys

def getMaxMonsters(n, hit, t, h):
    h.sort()
    curr_monster = 0
    max_hits = hit*t
    while not max_hits <= 0 and curr_monster < len(h):
        if h[curr_monster] > 0:
            h[curr_monster] -= hit
            max_hits -= hit
        else:
            curr_monster += 1
    if (curr_monster < len(h) and h[curr_monster] <= 0) or curr_monster >= len(h): 
        return curr_monster+1
    else:
        return curr_monster
    

n, hit, t = input().strip().split(' ')
n, hit, t = [int(n), int(hit), int(t)]
h = list(map(int, input().strip().split(' ')))
result = getMaxMonsters(n, hit, t, h)
print(result)