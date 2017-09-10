'''
Problem: Check Balanced
Description: Implement a function to check if a binary tree is balanced. For the purposes of this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.
Solved: True
'''

class Node(object):
    number = None
    left_child = None
    right_child = None

    def __init__(self, number):
        self.number = number

def check_balanced(node, height):
    if not node.left_child and not node.right_child:
        return height
    elif not node.left_child:
        return check_balanced(node.right_child, height+1)
    elif not node.right_child:
        return check_balanced(node.left_child, height+1)
    else:
        height_left = check_balanced(node.left_child, height+1)
        height_right = check_balanced(node.right_child, height+1)
        if not height_left or not height_right or not abs(height_left-height_right) <= 1:
            return False
        else:
            return max(height_left, height_right)