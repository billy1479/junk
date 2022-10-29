class Node:
    def __init__(self, data, before=None, after=None):
        self.data = data
        self.before = before
        self.after = after

class Stack:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def pop(self):
        output = self.head.data
        self.head = self.head.before
        return output
    def push(self, data):
        self.head = Node(data, self.head)
    def top(self):
        return self.head.data

polishString = input('Please enter the Polish Notation string: ')
polishStack = Stack()    

for x in polishString:
    if x == '+':
        value1 = int(polishStack.pop())
        value2 = int(polishStack.pop())
        answer = value1 + value2
        polishStack.push(answer)
    elif x == '-':
        value1 = int(polishStack.pop())
        value2 = int(polishStack.pop())
        answer = value1 - value2
        polishStack.push(answer)
    elif x == 'x':
        value1 = int(polishStack.pop())
        value2 = int(polishStack.pop())
        answer = value1 * value2
        polishStack.push(answer)
    elif x == '/':
        value1 = int(polishStack.pop())
        value2 = int(polishStack.pop())
        answer = value1 // value2
        polishStack.push(answer)
    else:
        polishStack.push(x)
print(polishStack.pop())