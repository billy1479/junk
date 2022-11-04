# This converts a hex number (with decimal) to its binary equivalent
from heapq import _heapify_max


base_array = [8,4,2,1]
hex_array = [['0',0], ['1',1], ['2',2],['3',3], ['4',4], ['5', 5], ['6',6], ['7', 7], ['8',8], ['9',9], ['A', 10],['B',11],['C',12],['D',13],['E',14],['F',15]]

myValue = input('Please enter in the hex value here: ')

# split the string into the integer and decimal part
x = []
y = []
temp_array = []
state = False
for i in myValue:
    if state == True:
        y.append(i)
    else:
        if i == '.':
            state = True
        else:
            x.append(i)

for a in x:
    for i in range(0, len(hex_array)):
        if hex_array[i][0] == a:
            hexValue = hex_array[i][1]
    
    state = False
    for z in range(3,-1,-1):
        if hexValue - base_array[z] > 0:
            temp_array.append('1')
        else:
            temp_array.append('0')

    
    


# calculate the sum of the decimal values




# join together with a decimal point





# output