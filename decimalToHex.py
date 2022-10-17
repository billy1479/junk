# take string of binary from decimal to binary scriptgit
from itertools import count
from math import ceil

data = input('Please enter in the decimal you want to be converted to Hexadecimal: ')
general_array = []
hex_array = [['0',0], ['1',1], ['2',2],['3',3], ['4',4], ['5', 5], ['6',6], ['7', 7], ['8',8], ['9',9], ['A', 10],['B',11],['C',12],['D',13],['E',14],['F',15]]

state = False
x = []
y = []
for i in data:
    if state == True:
        y.append(i)
    else:
        if i == '.':
            state = True
        else:
            x.append(i)

#in case no decimal is entered
if y==[]:
    y = ['0']

x = int(''.join(x))
y = float(''.join(y)) * 10**(-len(y))

# for X
temp_state = False
integer_array = []
decimal_state = []

# gets remainders and puts them in the integer_array
while temp_state == False:
    if x == 0:
        temp_state = True
    else:
        remainder = x % 16
        x = x // 16
        integer_array.append(remainder)

for x in range(len(integer_array)-1, -1, -1):
    temp2_state = False
    counter = 0
    while temp2_state == False:
        if integer_array[x] == hex_array[counter][1]:
            temp2_state = True
            integer_array[x] = hex_array[counter][0]
        else:
            temp2_state = False
            counter = counter + 1

integer_array = list(reversed(integer_array))

# for Y - will only allow exact fractions of 16 e.g. 0.625 or 0.5
temp_state = False
z = int(ceil(y * 16))
decimal_value = hex_array[z][0]

output = str(''.join(integer_array)) + str('.') + str(decimal_value)
print(output)





