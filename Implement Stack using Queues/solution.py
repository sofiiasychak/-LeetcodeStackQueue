class Queue:
    """Class representing Queue"""
    def __init__(self):
        '''Initialize an empty list to represent the queue'''
        self.queue = []

    def push(self, x):
        '''Add an element to the end of the queue'''
        self.queue.append(x)

    def pop(self):
        '''Remove and return the front element of the queue'''
        return self.queue.pop(0)

    def peek(self):
        '''Return the front element without removing it'''
        if self.is_empty():
            raise IndexError
        return self.queue[0]

    def size(self):
        '''Return the number of elements in the queue'''
        return len(self.queue)

    def is_empty(self):
        '''Check if the queue is empty'''
        return not self.queue


class MyStack(object):
    """Class implented by 2 queues."""
    def __init__(self):
        '''Initialize two queues to simulate a stack'''
        self.positive_queue = Queue()
        self.negative_queue = Queue()

    def push(self, x):
        '''Push an element onto the stack'''
        self.positive_queue.push(x)

    def pop(self):
        '''Remove and return the top element of the stack'''
        if self.empty():
            raise IndexError

        while self.positive_queue.size() > 1:
            self.negative_queue.push(self.positive_queue.pop())

        res = self.positive_queue.pop()
        self.positive_queue, self.negative_queue = self.negative_queue, self.positive_queue
        return res

    def top(self):
        '''Return the top element without removing it'''
        if self.empty():
            raise IndexError("Stack is empty")

        while self.positive_queue.size() > 1:
            self.negative_queue.push(self.positive_queue.pop())

        res = self.positive_queue.pop()
        self.negative_queue.push(res)
        self.positive_queue, self.negative_queue = self.negative_queue, self.positive_queue
        return res

    def empty(self):
        '''Check if the stack is empty'''
        return self.positive_queue.is_empty()
