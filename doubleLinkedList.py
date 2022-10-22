# This is a double linked list where each node will have a next and previous pointer
class Node:
    def __init__(self, data):
        self.next = None
        self.previous = None
        self.value = data

    def getNext(self):
        return self.next

    def getData(self):
        return self.value

    def getPrevious(self):
        return self.previous

