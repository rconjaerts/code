'''
Problem: Magic Index
Description: A magic index in an array A [0 ... n-1] is defined to be an index such that A[i] = i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.
Solved: True
'''

def find_magic_index(array, indexes):
    middle_index = len(array)/2

    if not array:
        return None
    elif array[middle_index] == indexes[middle_index]:
        return indexes[middle_index]
    elif len(array) == 1:
        return None
    elif array[middle_index] > indexes[middle_index]:
        return find_magic_index(array[:middle_index], indexes[:middle_index])
    else:
        return find_magic_index(array[middle_index:], indexes[middle_index:])

test_case = [-10, -5, -3, 0, 1, 2, 3, 7]
test_case2 = [5]
test_case3 = [-10, -5, -3, 0, 4, 10, 20, 30]
print(find_magic_index(test_case, range(len(test_case))))
print(find_magic_index(test_case2, range(len(test_case2))))
print(find_magic_index(test_case3, range(len(test_case3))))