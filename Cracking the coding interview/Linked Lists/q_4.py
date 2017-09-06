'''
Problem: Partition
Description: Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. lf x is contained within the list, the values of x only need to be after the elements less than x (see below). The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.
Solved: True
'''

class Node:
    next = None
    data = None

    def __init__(self, d):
        self.data = d

def partition_list(node, partition):
    first_low = None
    latest_low = None
    first_high = None
    curr_high = None

    while node:
        if node.data < partition and latest_low:
            latest_low.next = node
            lates_low = node
        elif node.data < partition:
            first_low = node
            latest_low = node
        elif first_high and curr_high:
            curr_high.next = node
            curr_high = node
        else:
            first_high = node
            curr_high = node

        node = node.next
    
    latest_low.next = first_high
    return first_low