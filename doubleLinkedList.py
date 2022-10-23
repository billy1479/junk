# This is a double linked list where each node will have a next and previous pointer
# Algorithm plan from 'Data Structures and Algorithms Python' - by Michael T. Goodrich, , Roberto Tamassia, , and Michael H. Goldwasse
class Node:
    def __init__(self, data, x, y):
        self.next = x
        self.previous = y
        self.value = data

class doubleLinkedList:
    # sets up the list with the two sentinel nodes pointing at each other
    def __init__(self):
        self.header = Node(None, None, None)
        self.trailer = Node(None, None, None)
        self.header.next = self.trailer
        self.trailer.previous = self.header
        self.size = 0

    # returns the length of the list
    def __len__(self):
        return self.size

    # returns a boolean value for if the list is empty or not
    def isEmpty(self):
        return self.size == 0

    # inserts an element in between two nodes and adjusts the pointers for it - returns the newly inserted node
    def insert_inbetween(self, data, predecessor, successor):
        newest = Node(data, successor, predecessor)
        predecessor.next = newest
        successor.prev = newest
        self.size = self.size + 1
        return newest

    # this deletes a node that has been specified and returns the data it holds
    def deleteNote(self, myNode):
        predecessor = myNode.previous
        successor = myNode.next
        predecessor.next = successor
        successor.previous = predecessor
        self.size = self.size - 1
        element = myNode.value
        myNode.next = myNode.previous = myNode.value = None
        return element