'''
Problem: List of Depths
Description: Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g., if you have a tree with depth 0, you'll have 0 linked lists).
Solved: True
'''

class GraphNode(object):
    value = None
    children = []

    def __init__(self, value):
        self.value = value

class LinkedListNode(object):
    value = None
    next = None

    def __init__(self, value):
        self.value = value

def create_list(nodes_at_depth):
    node = LinkedListNode(nodes_at_depth[0])
    first_node = node

    for i in range(1, len(nodes_at_depth)):
        new_node = LinkedListNode(nodes_at_depth[i])
        node.next = new_node
        node = new_node

    return first_node

def list_of_depths(root):
    curr_depth = [root]
    lists = []

    while curr_depth:
        lists.append(create_list(curr_depth))
        curr_depth = [child for el in curr_depth for child in el.children]

    return lists