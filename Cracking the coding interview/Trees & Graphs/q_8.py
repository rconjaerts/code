'''
Problem: First Common Ancestor
Description: Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree.
Solved: True
'''

class Node(object):
    def __init__(self, number):
        self.number = number
        self.left_child = None
        self.right_child = None

def find_common_ancestor(node, to_find_1, to_find_2):
    if node.number == to_find_1.number or node.number == to_find_2.number:
        return True
    elif not node.left_child and not node.right_child:
        return False
    elif not node.left_child:
        return find_common_ancestor(node.right_child, to_find_1, to_find_2)
    elif not node.right_child:
        return find_common_ancestor(node.left_child, to_find_1, to_find_2)
    else:
        left_subtree = find_common_ancestor(node.left_child, to_find_1, to_find_2)
        right_subtree = find_common_ancestor(node.right_child, to_find_1, to_find_2)

        if isinstance(left_subtree, Node):
            return left_subtree
        elif isinstance(right_subtree, Node):
            return right_subtree
        elif left_subtree and right_subtree:
            return node
        elif left_subtree or right_subtree:
            return True
        else:
            return False

# test case
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

print(find_common_ancestor(root, n2, n6).number)