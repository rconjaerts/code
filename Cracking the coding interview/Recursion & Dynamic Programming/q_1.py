'''
Problem: Triple Step
Description: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.
Solved: True
'''

def triple_step(n, d):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n in d:
        return d[n]
    else:
        d[n] = triple_step(n-1,d)+triple_step(n-2,d)+triple_step(n-3,d)
        return d[n]

print(triple_step(30, {}))