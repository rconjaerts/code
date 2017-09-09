'''
Problem: Stack Min
Description: How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop and min should all operate in 0(1) time.
Solved: True
''' 

class Stack:
    stack = None
    minimum = None

    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, el):
        self.minimum.append(el if not self.minimum or el < self.minimum[len(self.minimum)-1] else self.minimum[-1])
        self.stack.append(el)

    def pop(self):
        self.minimum = self.minimum[:len(self.minimum)-1]
        return self.stack.pop()

    def peek(self):
         return self.stack[len(self.stack)-1]

    def get_minimum(self):
        return self.minimum[-1]

    def is_empty(self):
        return self.stack == []