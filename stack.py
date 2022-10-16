# without an OOP approach
print('------------ Stack ------------')
stack_length = input('Please enter in the max length of the stack: ')
print('------------------')

myStack = ['Empty'] * int(stack_length)
front = stack_length - 1
size = 0

def is_Full():
    if size == stack_length - 1:
        return True
    else:
        return False
def is_Empty():
    if size == 0:
        return True
    else:
        return False

def show_stack():
    print('------------------')
    print('Showing contents of the stack...')
    counter = 0
    while counter != stack_length - 1:
        print(myStack[counter])
        counter += 1
    print('------------------')

def push(data):
    if is_Full():
        print('Error - stack overflow')
    else:
        front -= 1
        myStack[front] = data
        size += 1
        print('Data has been added to the top of the stack')

def pop():
    if is_Empty():
        print('Error - stack underflow')
    else:
        data = myStack[front]
        myStack[front] = 'Empty'
        front += 1
        size -= 1
        return data

def peek():
    if is_Empty():
        print('Error - stack underflow')
    else:
        data = myStack[front]
        return data

