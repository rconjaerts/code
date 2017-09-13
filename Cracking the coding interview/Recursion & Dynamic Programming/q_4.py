'''
Problem: Power Set
Description: Write a method to return all subsets of a set.
Notes: Not sure how to flatten the list
Solved: True
'''

import copy

def all_subsets(array, subsets, curr_solution):
    if not array:
        return curr_solution
    else:
        left_tree = all_subsets(array[1:], subsets, curr_solution)
        expanded_solution = copy.copy(curr_solution)
        expanded_solution.append(array[0])
        right_tree = all_subsets(array[1:], subsets, expanded_solution)
        return [left_tree, right_tree]

subsets = all_subsets([0, 1, 2], [], [])

for el in subsets:
    print(el) 