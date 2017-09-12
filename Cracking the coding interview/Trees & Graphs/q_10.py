'''
Problem: Check Subtree
DescripT1on: T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an algorithm to determine if T2 is a subtree of T1. A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2. That is, if you cut off the tree at node n, the two trees would be idenT1cal.
Solved: True
'''

class Node(object):
    def __init__(self, number):
        self.number = number
        self.left_child = None
        self.right_child = None

def find_node(tree, node):
    if not tree.left_child and not tree.right_child and tree.number != node.number:
        return None
    elif tree.number == node.number:
        return tree
    else:
        return max(find_node(tree.left_child, node), find_node(tree.right_child, node))

def compare_trees(t1, t2):
    if not t1.left_child and not t1.right_child and not t1.left_child and not t2.right_child and t1.number == t2.number:
        return True
    elif t1.number == t2.number:
        return min(compare_trees(t1.left_child, t2.left_child), compare_trees(t1.right_child, t2.right_child))
    else:
        return False

def check_subtree(t1, t2):
    # first find the root of t2 in t1. If it can't be found stop
    root_subtree_t1 = find_node(t1, t2)
    if root_subtree_t1:
        return 'T2 is a subtree of T1' if compare_trees(root_subtree_t1, t2) else 'Not a subtree'

    return 'Not a subtree'

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

root2 = Node(5)

n12 = Node(3)
n22 = Node(2)
n32 = Node(4)

n42 = Node(8)
n52 = Node(7)
n62 = Node(9)

root2.left_child = n12
root2.right_child = n42
n12.left_child = n22
n12.right_child = n32
n42.left_child = n52
n42.right_child = n62

# first one succeeds, second one fails
print(check_subtree(root, n4))
print(check_subtree(root, n42))