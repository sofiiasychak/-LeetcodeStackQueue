"""Implement Queue using Stacks"""
class Stack:
    """
    A basic implementation of a stack data structure.
    """
    def __init__(self):
        """
        Initializes an empty stack.
        """
        self.stack = []

    def push(self, x):
        """
        Adds an element to the top of the stack.
        """
        self.stack.append(x)

    def pop(self):
        """
        Removes and returns the element at the top of the stack.
        """
        if self.is_empty():
            raise IndexError
        return self.stack.pop()

    def peek(self):
        """
        Returns the element at the top of the stack without \
removing it.
        """
        if self.is_empty():
            raise IndexError
        return self.stack[-1]

    def size(self):
        """
        Returns the number of elements in the stack.
        """
        return len(self.stack)

    def is_empty(self):
        """
        Checks if the stack is empty.
        """
        return not self.stack

class MyQueue(object):
    """
    An implementation of a queue data structure using two stacks.
    This implementation follows the First-In-First-Out (FIFO) principle.
    """
    def __init__(self):
        """
        Initializes an empty queue with two stacks.
        """
        self.first_stack = Stack()
        self.second_stack = Stack()

    def push(self, x):
        """
        Adds an element to the back of the queue.
        """
        self.first_stack.push(x)

    def pop(self):
        """
        Removes and returns the element at the front of the queue.
        """
        if self.second_stack.is_empty():
            while not self.first_stack.is_empty():
                self.second_stack.push(self.first_stack.pop())
        return self.second_stack.pop()

    def peek(self):
        """
        Returns the element at the front of the queue without removing it.
        """
        if self.second_stack.is_empty():
            while not self.first_stack.is_empty():
                self.second_stack.push(self.first_stack.pop())
        return self.second_stack.peek()

    def empty(self):
        """
        Checks if the queue is empty.
        """
        return self.first_stack.is_empty() and self.second_stack.is_empty()
