'''
Problem: Recursive Multiply
Description: Write a recursive function to multiply two positive integers without using the * operator. You can use addition, subtraction, and bit shifting, but you should minimize the number of those operations.
Solved: True
'''

# O(n)
def recursive_multiply_simple(x, y):
    count = 0
    while y != 0:
        count += x
        y -= 1
    return count

# O(log(n)) is possible if we use bit manipulation to divide by 2
def recursive_multiply(x, y):
    if x == 0:
        return 0
    elif x == 1:
        return y

    s = x >> 1
    half_prod = recursive_multiply(s, y)

    if x%2 == 0:
        return half_prod+half_prod
    else:
        return half_prod+half_prod+y

print(recursive_multiply(5, 8))
