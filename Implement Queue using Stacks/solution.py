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
    
class MyQueue(object):
    def __init__(self):
        self.first_stack = Stack()
        self.second_stack = Stack()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.first_stack.push(x)

    def pop(self):
        """
        :rtype: int
        """
        if self.second_stack.is_empty():
            while not self.first_stack.is_empty():
                self.second_stack.push(self.first_stack.pop())
        return self.second_stack.pop()

    def peek(self):
        """
        :rtype: int
        """
        if self.second_stack.is_empty():
            while not self.first_stack.is_empty():
                self.second_stack.push(self.first_stack.pop())
        return self.second_stack.peek()
        

    def empty(self):
        """
        :rtype: bool
        """
        return self.first_stack.is_empty() and self.second_stack.is_empty()
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()