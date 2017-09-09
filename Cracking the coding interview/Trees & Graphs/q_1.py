'''
Problem: Route Between Nodes
Description: Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
Solved: True
'''

class Queue(object):
    queue = None

    def __init__(self):
        self.queue = []

    def enqueue(self, el):
        self.queue.insert(0, el)

    def dequeue(self):
        return self.queue.pop()

class Node(object):
    name = None
    adjacents = []
    visited = False

    def __init__(self, name):
        self.name = name

def find_path(from_node, to_node):
    q = Queue()
    q.enqueue(node1)

    while q.queue:
        n1 = q.dequeue()
        if n1 == node2:
            return True
        else:
            n1.visited = True
            for x in n1.adjacents:
                if not x.visited:
                    q.enqueue(x)

    return False

def has_connection(node1, node2):
    # since it's a directed graph, we have to look in both directions
    return find_path(node1, node2) or find_path(node2, node1)