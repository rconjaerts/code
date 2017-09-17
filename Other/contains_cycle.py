class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next  = None

def contains_cycle(head):
    visited = []
    while head:
        if head in visited:
            return True
        else:
            visited.append(head)
        head = head.next
    return False

ll1 = LinkedListNode(1)
ll2 = LinkedListNode(2)
ll3 = LinkedListNode(3)
ll4 = LinkedListNode(4)
ll5 = LinkedListNode(5)
ll6 = LinkedListNode(6)
ll7 = LinkedListNode(7)
ll8 = LinkedListNode(8)

ll1.next = ll2
ll2.next = ll3
ll3.next = ll4
ll4.next = ll5
ll5.next = ll6
ll6.next = ll7
ll7.next = ll8
#ll8.next = ll4

print(contains_cycle(ll1))