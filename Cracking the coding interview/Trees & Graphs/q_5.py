'''
Problem: Validate BST
Description: Implement a function to check if a binary tree is a binary search tree.
Solved: True
'''

class Node(object):
    number = None
    left_child = None
    right_child = None

    def __init__(self, number):
        self.number = number

def validate_bst(node, type):
    if not node.left_child and not node.right_child:
        return node.number
    elif not node.left_child:
        right = validate_bst(node.right_child, 'right_child')
        if right < node.number:
            return False
        else:
            return min(right, node.number)
    elif not node.right_child:
        left = validate_bst(node.left_child, 'left_child')
        if left > node.number:
            return False
        else:
            return max(left, node.number)
    else:
        max_left = validate_bst(node.left_child, 'left_child')
        min_right = validate_bst(node.right_child, 'right_child')

        if node.number <= min_right and node.number >= max_left:
            return min(node.number, max_left, min_right) if type == 'right_child' else max(node.number, max_left, min_right)
        else:
            return False

# test case. Change value of n3 to 20 to test if it would fail
root = Node(5)

n1 = Node(3)
n2 = Node(2)
n3 = Node(4)

n4 = Node(8)
n5 = Node(7)
n6 = Node(10)

root.left_child = n1
root.right_child = n4
n1.left_child = n2
n1.right_child = n3
n4.left_child = n5
n4.right_child = n6

print(bool(validate_bst(root, 'root')))