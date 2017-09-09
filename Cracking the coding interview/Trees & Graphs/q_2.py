'''
Problem: Minimal Tree
Description: Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.
Solved: True
'''

class Node(object):
    number = None
    left_child = None
    right_child = None

    def __init__(self, number):
        self.number = number

def create_bst(sorted_array):
    if not sorted_array:
        return None
    elif len(sorted_array) == 1:
        return Node(sorted_array[0])
    else:
        index = len(sorted_array)/2
        middle = sorted_array[index]
        left = sorted_array[:index]
        right = sorted_array[index+1:]
        node = Node(middle)
        node.left_child = create_bst(left)
        node.right_child = create_bst(right)
        return node