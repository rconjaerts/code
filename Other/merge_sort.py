'''
Problem: Merge Sort
Description: Implement merge sort to learn how it works
Solved: True
'''

def sort_halves(left, right):
    helper = []
    l_i = 0
    r_i = 0

    while l_i < len(left) and r_i < len(right):
        if left[l_i] <= right[r_i]:
            helper.append(left[l_i])
            l_i += 1
        else:
            helper.append(right[r_i])
            r_i += 1

    helper.extend(left[l_i:] if l_i < len(left) else right[r_i:])
    return helper

def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr)/2
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        return sort_halves(left, right)
    else:
        return arr

test_even = [5, 2, 8, 6, 1, 6, 3, 1, 7, 9]
test_uneven = [5, 2, 8, 6, 1, 6, 3, 1, 7]

print(merge_sort(test_even))
print(merge_sort(test_uneven))