# working
class circularQueue:
    def __init__(self, a):
        self.cqueue = []
        for x in range(0, a):
            self.cqueue.append('Empty')
        self.front = 0
        self.rear = -1
        self.size = 0
        self.maxSize = int(a)
    
    def is_full(self):
        if self.size == self.maxSize:
            return True
        else:
            return False
    
    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def enqueue(self, data):
        if self.is_full():
            print('The queue is full')
        else:
            self.rear = (self.rear + 1) % self.maxSize
            self.cqueue[self.rear] = data
            self.size = self.size + 1

    def dequeue(self):
        if self.is_empty():
            print('The queue is empty')
        else:
            data = self.cqueue[self.front]
            self.front = self.front + 1
            self.size = self.size - 1
            return data

queueSize = 5
queueA = circularQueue(queueSize)

