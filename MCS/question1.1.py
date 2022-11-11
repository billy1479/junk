import random
import math

def multiply(x):
    return multiple * x

# This is from linear algebra week 6
matrix1 = []
matrix2 = []

# fills out matrix 1 and matrix 2
for x in range(0,3):
    matrix1.append(random.randint(-5,5))
    matrix2.append(random.randint(-5,5))

multiple = random.randint(-3,3)

matrix1 = map(multiply, matrix1)
matrix2 = map(multiply, matrix2)

