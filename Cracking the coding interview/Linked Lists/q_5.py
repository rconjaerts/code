'''
Problem: Sum Lists
Description: You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
FOLLOW UP: Suppose the digits are stored in forward order. Repeat the above problem.
Solved: True
'''

class Node:
    next = None
    data = None

    def __init__(self, d):
        self.data = d

def get_number(node):
    count = 1
    total = node.data
    node = node.next

    while node:
        total += node.data*10**count
        count += 1
        node = node.next
    
    return total

def create_reverse_from_number(number):
    node = Node(number-int(number/10)*10)
    first_node = node
    number = int(number/10)

    while number != 0:
        new_node = Node(number-int(number/10)*10)
        number = int(number/10)
        node.next = new_node
        node = new_node
    
    return first_node

def create_from_number(number):
    l = len(str(number))
    curr_number = number/(10**(l-1))
    number -= curr_number*(10**(l-1))
    node = Node(curr_number)
    first_node = node

    while number != 0:
        l = len(str(number))
        curr_number = number/(10**(l-1))
        number -= curr_number*(10**(l-1))
        new_node = Node(curr_number)
        node.next = new_node
        node = new_node
    
    return first_node

def sum_linked_lists(head1, head2):
    n1 = get_number(head1)
    n2 = get_number(head2)
    the_sum = n1+n2

    head_reverse = create_reverse_from_number(the_sum)
    head_correct = create_from_number(the_sum)

# test cases worked
t1 = Node(7)
t2 = Node(1)
t3 = Node(6)
t1.next = t2
t2.next = t3

t4 = Node(5)
t5 = Node(9)
t6 = Node(2)
t4.next = t5
t5.next = t6

sum_linked_lists(t1, t4)