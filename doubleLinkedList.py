# This is a double linked list where each node will have a next and previous pointer
class Node:
    def __init__(self, data, x, y):
        self.next = x
        self.previous = y
        self.value = data

class doubleLinkedList:
    def __init__(self):
        self.header = Node
