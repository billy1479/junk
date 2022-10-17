# take string of binary from decimal to binary scriptgit
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

# gets remainders and puts them in the ineger_array
while temp_state == False:
    if x == 0:
        temp_state = True
    else:
        remainder = x % 16
        x = x // 16
        integer_array.append(remainder)

for x in range(len(integer_array), -1, -1):
    


