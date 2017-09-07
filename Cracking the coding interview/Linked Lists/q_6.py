'''
Problem: Palindrome
Description: Implement a function to check if a linked list is a palindrome.
Solved: True
'''

class Node:
    next = None
    data = None

    def __init__(self, d):
        self.data = d

def is_palindrome(node):
    word = []

    while node:
        word.append(node.data)
        node = node.next
    
    p1 = word[:len(word)/2]
    p2 = None

    if len(word)%2 == 0:
        p2 = word[len(word)/2:]
    else:
        p2 = word[len(word)/2+1:]
        
    p2.reverse()
    return True if p1 == p2 else False