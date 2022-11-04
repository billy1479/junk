import string

hex_array = [['0',0], ['1',1], ['2',2],['3',3], ['4',4], ['5', 5], ['6',6], ['7', 7], ['8',8], ['9',9], ['A', 10],['B',11],['C',12],['D',13],['E',14],['F',15]]

def positive_hex_array(string_length):
    temp_array = []
    for i in range(string_length-1, -1, -1):
        temp_array.append(16**i)
    return temp_array

def decimal_hex_array(string_length):
    temp_array = []
    for i in range(1, string_length+1):
        temp_array.append(16**-i)
    return temp_array

hex_string = input('Please enter in the Hexadecimal string : ') 
decimalState = False

x = []
y = []

for a in hex_string:
    if decimalState == True:
        y.append(a)
    else:
        if a == '.':
            decimalState = True
        else:
            x.append(a)

a = positive_hex_array(len(x))
b = decimal_hex_array(len(y))

front_total = 0
back_total = 0

for i in range(0, len(x)):
    temp_state = False
    counter = 0
    while temp_state == False and counter <= len(hex_array):
        if hex_array[counter][0] == x[i]:
            front_total = front_total + (hex_array[counter][1] * a[i])
            temp_state = True
        else:
            counter += 1

for i in range(0, len(y)):
    temp_state = False
    counter = 0
    while temp_state == False and counter <= len(hex_array):
        if hex_array[counter][0] == y[i]:
            back_total = back_total + (hex_array[counter][1] * b[i])
            temp_state = True
        else:
            counter += 1


print('The total is : ' + str(front_total + back_total))
