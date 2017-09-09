'''
Problem: Return Kth to Last
Description: Implement an algorithm to find the kth to last element of a singly linked list.
Solved: True
'''

class Node:
    next = None
    data = None

    def __init__(self, d):
        self.data = d

def get_k_to_last(node, k):
    p1 = node
    p2 = node
    count = k

    # we first find the k-th element from the start
    while count != 0:
        count -= 1
        p2 = p2.next

    # we go all the way to the end with p2 and return p1 since the distance between p1 and p2 is exact k
    while p2.next:
        p1 = p1.next
        p2 = p2.next
    
    return p1