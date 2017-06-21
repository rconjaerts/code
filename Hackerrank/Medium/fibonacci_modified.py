'''
Problem: https://www.hackerrank.com/challenges/fibonacci-modified
Solved: True
'''

t1, t2, n = input().split(" ")
t1,t2,n = int(t1), int(t2), int(n)

# n > 2 because we start from t1, and t2
while n > 2:
    t1, t2 = t2, t1+(t2**2)
    n -= 1
    
print(t2)
