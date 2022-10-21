# THIS IS A SINGLE LINKED LIST
class Node:
    def __init__(self, data):
        self.data = data
        self.pointer = None

    def set_pointer(self, newPointer):
        self.pointer = newPointer

    def get_data(self):
        return self.data

    def get_next(self):
        return self.pointer

class linkedList:
    def __init__(self):
        self.head = None

    def insert_into_list(self, data):
        # puts data at the front of the list
        myNode = Node(data)
        if self.head == None:
            self.head = myNode
        else:
            myNode.set_pointer(self.head)
            self.head = myNode

    def insert_in_order(self, data):
        myNode = Node(data)
        current = self.head

        if self.head == None:
            self.head = myNode
        elif myNode.get_data() < current.get_data():
            myNode.set_pointer(self.head)
            self.head = myNode
        else:
            while (current.get_next() is not None and current.get_next().get_data() < myNode.get_data()):
                current = current.get_next()

            myNode.set_pointer(current.get_next())
            current.set_pointer(myNode)

    def traverseList(self):
        current = self.head
        while current is not None:
            print(current.get_data())
            current = current.get_next()

    def delete(self, data):
        current = self.head
        if current.get_data() == data:
            self.head = current.get_next()
        else:
            while current.get_next().get_data() != data:
                current = current.get_next()
            current.set_pointer(current.get_next().get_next())
 
state = False
# 1,2,3,4 are the modes for adding an item to the head of the list, adding a item into the list in an ordered position, printing the list and deleting an item
while state == False:
    print('Please enter mode 1,2,3 or 4 for starting a list, adding an item to the list, print the list and delete an item from the list respectively')
    print('Please enter in mode 5 if you want to end the program')
    print('--------- -------- --------- ----------')
    print('--------- -------- --------- ----------')
    print('--------- -------- --------- ----------')
    print('--------- -------- --------- ----------')
    mode = input('Please enter in the mode : ')
    print('--------- -------- --------- ----------')
    if mode == 1:
        myList = linkedList()
        print('Linked list has been created.')
    elif mode == 2: 
        
    elif mode == 3:

    elif mode == 4:

    elif mode == 5:
        print('You have chosen to end the program')
        state = True
    else:
        print('Please enter in the correct mode.')
