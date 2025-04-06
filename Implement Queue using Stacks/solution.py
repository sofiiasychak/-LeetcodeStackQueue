class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)
    
    def pop(self):
        if self.is_empty():
            raise IndexError
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return not self.stack
    

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()