# This converts a hex number (with decimal) to its binary equivalent
from heapq import _heapify_max


base_array = [8,4,2,1]
hex_array = [['0',0], ['1',1], ['2',2],['3',3], ['4',4], ['5', 5], ['6',6], ['7', 7], ['8',8], ['9',9], ['A', 10],['B',11],['C',12],['D',13],['E',14],['F',15]]

myValue = input('Please enter in the hex value here: ')

# split the string into the integer and decimal part
x = []
y = []
state = False
for i in myValue:
    if state == True:
        y.append(i)
    else:
        if i == '.':
            state = True
        else:
            x.append(i)

# calculate sum of all integer values
# can be more efficient with a while loop
integerTotal = 0
lengthOfInteger = len(x)
for a in x:
    for i in range(0, len(hex_array)):
        if hex_array[]

# calculate the sum of the decimal values




# join together with a decimal point





# output