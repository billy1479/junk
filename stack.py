class myStack:
    def __init__(self, size):
        # Initialises an array of size 'size' where each element is 'empty' and sets the head to -1
        self.size = size
        self.stack = ['Empty'] * size
        self.head = -1

    def showStack(self):
        # outputs the contents of the stack
        for i in self.stack:
            print(i)

    def pop(self):
        data = self.stack[self.head]
        self.stack[self.head] = 'Empty'
        self.head = self.head - 1
        return data
    
    def peek(self):
        return self.stack[self.head]
    