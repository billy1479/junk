# This is a binary converter that changes a binary string of as many units as possible with decimals into its denary format
from turtle import back


def power_of_two(a):
    temp_array = []
    for i in range(a-1,0-1,-1):
        temp_array.append(2**i)
    return temp_array

def decimal(a):
    temp_array = []
    for i in range(1, a+1):
        temp_array.append(2**-i)
    return temp_array

binary_string = input('Please enter in your binary string here:  ')
binary_string = str(binary_string)
binary_length = len(binary_string)

state = False
x = []
y = []

for i in binary_string:
    if state==True:
        y.append(i)
    else:
        if i=='.':
            state = True
        else:
            x.append(i)


front_total = 0
back_total = 0

power_of_two_array = power_of_two(len(x))
decimal_array = decimal(len(y))

for i in range(0, len(x)):
    if x[i] == '1':
        front_total = front_total + power_of_two_array[i]

for c in range(0, len(y)):
    if y[c] == '1':
        back_total = back_total + decimal_array[c]

output = front_total + back_total
print(output)