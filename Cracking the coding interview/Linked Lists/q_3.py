'''
Problem: Delete Middle Node
Description: Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.
Solved: True
'''

class Node:
    next = None
    data = None

    def __init__(self, d):
        self.data = d

def delete_node(node):
    # we copy the data from the next node into our own
    node.data = node.next.data
    # we replace the next node by the one after the next node
    node.next = node.next.next