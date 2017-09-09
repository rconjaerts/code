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
    all_data = set()

    while node:
        if node.data in all_data:
            prev.next = node.next
            prev = node
        else:
            all_data.add(node.data)
            prev = node
        node = node.next