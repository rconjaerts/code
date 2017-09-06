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

def find_node_k(node, k, count):
    if k == count:
        return node
    elif node.next:
        find_node_k(node.next, k, count+1)
    else:
        return None

def get_k_to_last(node, k):
    node_k = find_node_k(node, k, 0)

    if node_k:
        all_nodes = []
        while node.next:
            all_nodes.append(node)
            node = node.next
        all_nodes.append(node)
        return all_nodes
    else:
        return False

k = 5
k_to_last = get_k_to_last(head, k)