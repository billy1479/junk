n = int(input('Please enter in the value of n: '))

def question2Function(n):
    for x in range(1, n):
        value = (1 + ((-1)**x / x**2))
        print(str(x) + ': ' + str(value))

question2Function(n)