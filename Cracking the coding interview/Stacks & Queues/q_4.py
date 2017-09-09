'''
Problem: Queue via stacks
Description: Implement a MyQueue class which implements a queue using two stacks.
Solved: True
'''

class MyQueue:
    to_add = None
    to_remove = None
    last_pop = False

    def __init__(self, size):
        self.to_add = Stack()
        self.to_remove = Stack()

    def add(self, el):
        if last_pop:
            while self.to_remove:
                self.to_add.push(self.to_remove.pop())

        last_pop = False
        self.to_add.push(el)
    
    def remove(self):
        if not last_pop:
            while self.to_add:
                self.to_remove.push(self.to_add.pop())
        
        last_pop = True
        return self.to_remove.pop()

    def peek(self):
        if not last_pop:
            while self.to_add:
                self.to_remove.push(self.to_add.pop())
        
        last_pop = True
        return self.to_remove.peek()

class Stack:
    stack = None

    def __init__(self):
        self.stack = []

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        return self.stack.pop()

    def peek(self):
         return self.stack[len(self.stack)-1]

    def is_empty(self):
        return self.stack == []