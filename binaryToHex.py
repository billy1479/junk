# only lets up to 4 bits for the decimal part
# as many bits for the integer part
from email.mime import base


print('Please ensure there are no more than 4 bits after the decimal point - any extra will be ignored.')
binary_string = input('Please enter in the binary string: ')

base_array = [8,4,2,1]
hex_array = [['0',0], ['1',1], ['2',2],['3',3], ['4',4], ['5', 5], ['6',6], ['7', 7], ['8',8], ['9',9], ['A', 10],['B',11],['C',12],['D',13],['E',14],['F',15]]


# This splits the binary string into integer and decimal part
state = False
x = []
y = []
decimal_counter = 1

for i in binary_string:
    if state==True:
        if decimal_counter > 4:
            break
        else:
            y.append(i)
            decimal_counter += 1
    else:
        if i=='.':
            state = True
        else:
            x.append(i)

general_array = []
temp_array = []
counter = -1
for value in x:
    if counter == 3:
        general_array.append(temp_array)
        counter = 0
        temp_array = []
        temp_array.append(value)
    else:
        temp_array.append(value)
        counter += 1

general_array.append(temp_array)


for i in range(0, len(general_array) - 1):
    total = 0
    for x in range(len(base_array)-1, -1, -1):
        if general_array[i] == '1':
            total = total + base_array[i]
    hexValue = hex_array[total][1]
            
