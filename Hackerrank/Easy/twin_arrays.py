'''
Problem: https://www.hackerrank.com/contests/w33/challenges/twin-arrays
Solved: True
'''

#!/bin/python3

import sys

def twinArrays(ar1, ar2):
    min1_1 = float('inf')
    ind1_1 = 0
    min1_2 = float('inf')
    ind1_2 = 0
    min2_1 = float('inf')
    ind2_1 = 0
    min2_2 = float('inf')
    ind2_2 = 0
    
    for i in range(len(ar1)):
        if ar1[i] < min1_1:
            min1_1, min1_2 = ar1[i], min1_1
            ind1_1, ind1_2 = i, ind1_1
        elif ar1[i] < min1_2:
            min1_2 = ar1[i]
            ind1_2 = i
            
    for i in range(len(ar2)):
        if ar2[i] < min2_1:
            min2_1, min2_2 = ar2[i], min2_1
            ind2_1, ind2_2 = i, ind2_1
        elif ar2[i] < min2_2:
            min2_2 = ar2[i]
            ind2_2 = i
              
    if ind1_1 != ind2_1:
        return min1_1+min2_1
    else:
        return min2_1+min1_2 if min2_1+min1_2 < min1_1+min2_2 else min1_1+min2_2

n = int(input().strip())
ar1 = list(map(int, input().strip().split(' ')))
ar2 = list(map(int, input().strip().split(' ')))
result = twinArrays(ar1, ar2)
print(result)