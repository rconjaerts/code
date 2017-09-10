'''
Problem: Successor
Description: Write an algorithm to find the "next" node (i .e., in-order successor) of a given node in a binary search tree. You may assume that each node has a link to its parent.
Solved: True
'''

class Node(object):
    number = None
    left_child = None
    right_child = None
    parent = None

    def __init__(self, number):
        self.number = number

# we do the search by number, not by object since the exercise specifically says BST
def find_successor(node):
    if not node:
        return None

    if node.right_child:
        return find_left_most_child(node.right_child)
    else:
        c = node
        p = node.parent

        while(p and p.left_child != c):
            c = p
            p = c.parent
        return p

def find_left_most_child(node):
    while node.left_child:
        node = node.left_child
    return node

# test case
root = Node(5)

n1 = Node(3)
n2 = Node(2)
n3 = Node(4)

n4 = Node(8)
n5 = Node(7)
n6 = Node(10)

root.left_child = n1
n1.parent = root
root.right_child = n4
n4.parent = root
n1.left_child = n2
n2.parent = n1
n1.right_child = n3
n3.parent = n1
n4.left_child = n5
n5.parent = n4
n4.right_child = n6
n6.parent = n4

print(find_successor(root).number)