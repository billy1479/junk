from itertools import count
import math

from conversions.binarytodecimal import decimal
decimal_value = input('Please enter in the decimal value here: ')

# Breaks down the input into the integer part and the decimal part
state = False
x = []
y = []
for i in decimal_value:
    if state == True:
        y.append(i)
    else:
        if i == '.':
            state = True
        else:
            x.append(i)
    
integerPart = int(''.join(x))
decimalPart = float(''.join(y)) - 1

integerLog = math.log(integerPart, 2)
integerLog = math.ceil(integerLog)
decimalLog = math.log(decimalPart, 2)
decimalLog = math.ceil(decimalLog)

integer_array = []
decimal_array = []

for i in range(integerLog, -1, -1):
    integer_array.append(2**i)

for i in range(1, decimalLog):
    decimal_array.append(2**-i)

binary_array = []

# for the integer part of the string
temp_state = False
counter = 0
while temp_state == False and counter < len(integer_array):
    if (integerPart-integer_array[counter]) > 0:
        binary_array.append('1')
        integerPart = integerPart - integer_array[counter]
        counter += 1
    elif (integerPart-integer_array[counter]) == 0:
        binary_array.append('1')
        integerPart = integerPart - integer_array[counter]
        temp_state = True
        counter += 1
    else:
        binary_array.append('0')
        counter += 1

binary_array.append('.')

temp_state = False
counter = 0
while temp_state == False and counter < len(decimal_array):
    if (decimalPart-decimal_array[counter]) > 0:
        binary_array.append('1')
        decimalPart = decimalPart - decimal_array[counter]
        counter += 1
    elif (decimalPart-decimal_array[counter]) == 0:
        binary_array.append('1')
        decimalPart = decimalPart - decimal_array[counter]
        temp_state = True
    else:
        binary_array.append('0')
        counter += 1
    
print(''.join(binary_array))



