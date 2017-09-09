'''
Problem: Stack of Plates
Description: Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity. SetOfStacks. push () and SetOfStacks. pop () should behave identically to a single stack (that is, pop ( ) should return the same values as it would if there were just a single stack).
Solved: True
'''

class SetOfStacks:
    max_stack_size = None
    all_stacks = None

    def __init__(self, size):
        self.max_stack_size = size
        self.all_stacks = [Stack()]

    def push(self, el):
        curr_stack = self.all_stacks[-1]

        if len(curr_stack) = self.max_stack_size:
            new_stack = Stack()
            new_stack.push(el)
            all_stacks.append(new_stack)
        else:
            curr_stack.append(el)

    def pop(self):
        curr_stack = self.all_stacks[-1]
        el = curr_stack.pop()
        if len(curr_stack) == 0:
            self.all_stacks = self.all_stacks[:-1]
        return el

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