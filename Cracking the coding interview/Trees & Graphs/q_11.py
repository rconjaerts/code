'''
Problem: Random Node
DescripT1on: You are implementing a binary tree class from scratch which, in addition to insert, find, and delete, has a method getRandomNode() which returns a random node from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm for getRandomNode, and explain how you would implement the rest of the methods.
Solved: True
'''

import random

class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, el):
        self.queue.insert(0, el)

    def dequeue(self):
        return self.queue.pop()

class Node(object):
    def __init__(self, number):
        self.number = number
        self.left_child = None
        self.right_child = None

class Tree(object):
    def __init__(self):
        self.root = None
        self.number_of_nodes = 0

    def find_parent(self, root, node):
        if not root:
            return None
        elif root.left_child == node or root.right_child == node:
            return root
        elif not root.left_child and not root.right_child:
            return None
        else:
            return max(self.find_parent(root.left_child, node), self.find_parent(root.right_child, node))

    def __search_tree(self, root, numb):
        if root.number == numb:
            return root
        elif not root.left_child and not root.right_child:
            return None
        elif not root.left_child:
            return self.__search_tree(root.right_child, numb)
        elif not root.right_child:
            return self.__search_tree(root.left_child, numb)
        else:
            return max(self.__search_tree(root.left_child, numb), self.__search_tree(root.right_child, numb))

    def find(self, numb):
        return self.__search_tree(self.root, numb)
    
    def __insert_node_in_tree(self, root, node):
        queue = Queue()
        queue.enqueue(root)

        while queue.queue:
            next_level = []
            for el in queue.queue:
                if not el.left_child:
                    el.left_child = node
                    return
                elif not el.right_child:
                    el.right_child = node
                    return
                else:
                    next_level.append(el.left_child)
                    next_level.append(el.right_child)

            queue.queue = next_level
        return False

    def insert(self, numb):
        new_node = Node(numb)
        self.__insert_node_in_tree(self.root, new_node)
        self.number_of_nodes += 1

    def __find_node_by_index(self, root, node_number):
        queue = Queue()
        queue.enqueue(root)

        while node_number > 0:
            curr_el = queue.dequeue()
            queue.enqueue(curr_el.left_child)
            queue.enqueue(curr_el.right_child)
            node_number -= 2

        if node_number == 0:
            return queue.dequeue()
        else:
            queue.dequeue()
            return queue.dequeue()

    def get_random_node(self):
        node_number = random.randint(0, self.number_of_nodes)
        return self.find_node_by_index(self.root, node_number)

root = Node(5)

n1 = Node(3)
n2 = Node(2)
n3 = Node(4)

n4 = Node(8)
n5 = Node(7)
n6 = Node(10)

root.left_child = n1
root.right_child = n4
n1.left_child = n2
n1.right_child = n3
#n4.left_child = n5
#n4.right_child = n6

tree = Tree()
tree.root = root
print(tree.find(4))
tree.insert(7)
print(tree.find(7))
tree.delete(n3)