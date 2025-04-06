class Queue:
    def __init__(self):
        self.queue = []

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return not self.queue

