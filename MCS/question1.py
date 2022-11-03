a = int(input('Please enter in the value of a:  '))
n = int(input('Please enter in the value of n: '))
start = int(input('Please enter in the start value: '))
counter = 0

def question1Function(a, counter, x):
    if counter == n:
        value = 0.5 * (x + (a//x))
        print(value)
    else:
        value = 0.5 * (x + (a//x))
        print(value)
        return question1Function(a, counter + 1, value)

question1Function(a, counter, start)
