'''
Problem: https://www.hackerrank.com/challenges/the-power-sum
Solved: True

Notes: We could improve the performance by using dynamic programming
'''

x = int(input().strip())
n = int(input().strip())

def  findSum(curr_val, curr_sum):
    if curr_sum+(curr_val**n) == x:
        return 1
    elif curr_val**n > x or curr_sum+(curr_val**n) > x:
        return 0
    else:
        return findSum(curr_val+1, curr_sum+curr_val**n)+findSum(curr_val+1, curr_sum)
    
print(findSum(1, 0))
