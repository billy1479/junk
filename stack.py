class myStack:
    def __init__(self, size):
        # Initialises an array of size 'size' where each element is 'empty' and sets the head to -1
        self.size = 0
        self.maxSize = size
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

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def push(self, x):
        if self.size == self.maxSize:
            print('The stack is full - no more items can be added')
        else:
            self.size += 1
            self.head += 1
            self.stack[self.head] = x
    