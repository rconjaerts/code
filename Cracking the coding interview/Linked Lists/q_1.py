'''
Problem: Remove Dups
Description: Write code to remove duplicates from an unsorted linked list. How would you solve this problem if a temporary buffer is not allowed?
Solved: True
'''

class Node:
    next = None
    data = None

    def __init__(self, d):
        self.data = d

def remove_duplicates(node, prev):
    if node.data in all_data:
        prev.next = node.next
        if node.next:
            remove_duplicates(node.next, prev)
    else:
        all_data.add(node.data)
        if node.next:
            remove_duplicates(node.next, node)

all_data = set()