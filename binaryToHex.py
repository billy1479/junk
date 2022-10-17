# only lets up to 4 bits for the decimal part
# as many bits for the integer part
print('Please ensure there are no more than 4 bits after the decimal point - any extra will be ignored.')
binary_string = input('Please enter in the binary string: ')

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

