'''
Problem: Paths with Sum
DescripT1on: You are given a binary tree in which each node contains an integer value (which might be positive or negative). Design an algorithm to count the number of paths that sum to a given value. The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
Solved: True
'''

class Node(object):
    def __init__(self, number):
        self.number = number
        self.left_child = None
        self.right_child = None

def paths_with_sum(node, sum, curr_sum):
    if not node:
        return 0
    elif node.number+curr_sum == sum:
        return 1+paths_with_sum(node.left_child, sum, curr_sum+node.number)+paths_with_sum(node.right_child, sum, curr_sum+node.number)+paths_with_sum(node.left_child, sum, curr_sum)+paths_with_sum(node.right_child, sum, curr_sum)
    else:
        return paths_with_sum(node.left_child, sum, curr_sum)+paths_with_sum(node.right_child, sum, curr_sum)+paths_with_sum(node.left_child, sum, curr_sum+node.number)+paths_with_sum(node.right_child, sum, curr_sum+node.number)

# test case
root = Node(5)

n1 = Node(3)
n2 = Node(2)
n3 = Node(4)

n4 = Node(8)
n5 = Node(7)
n6 = Node(10)
n7 = Node(1)

root.left_child = n1
root.right_child = n4
n1.left_child = n2
n1.right_child = n3
n4.left_child = n5
n4.right_child = n6
n5.left_child = n7

print(paths_with_sum(root, 8, 0))