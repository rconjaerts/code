'''
Problem: Sort Stack
Description: Write a program to sort a stack such that the smallest items are on the top. You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.
Solved: True
'''

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

    def sort(self):
        temp_stack = Stack()

        while not self.stack.is_empty():
            temp = self.stack.pop()
            while not temp_stack.is_empty() and temp_stack.peek() > temp:
                self.stack.push(temp_stack.pop())
            temp_stack.push(temp)

        while not temp_stack.is_empty():
            self.stack.push(temp_stack.pop())