'''
Problem: Loop Detection
Description: Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.
Solved: True
'''

class Node:
    next = None
    data = None
    visited = False

    def __init__(self, d):
        self.data = d

def find_loop(node1):
    while node1:
        if node1.visited:
            return node1
        else:
            node1.visited = True
            node1 = node1.next

    # in case it's not a circular list
    return None