'''
Problem: Intersection
Description: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection is defined based on reference, not value. That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting.
Solved: True
'''

class Node:
    next = None
    data = None
    visited = False

    def __init__(self, d):
        self.data = d

def find_intersect(node1, node2):
    while node1:
        node1.visited = True
        node1 = node1.next

    while node2:
        if node2.visited:
            return node2
        else:
            node2 = node2.next

    return None