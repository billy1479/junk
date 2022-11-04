from turtle import back
import math
from math import ceil
from itertools import count


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

base_array = [8,4,2,1]
hex_array = [['0',0], ['1',1], ['2',2],['3',3], ['4',4], ['5', 5], ['6',6], ['7', 7], ['8',8], ['9',9], ['A', 10],['B',11],['C',12],['D',13],['E',14],['F',15]]

class Binary:
    def __init__(self, data):
        self.binaryValue = data
        state = False
        x = []
        y = []

        for i in data:
            if state==True:
                y.append(i)
            else:
                if i=='.':
                    state = True
                else:
                    x.append(i)
        self.integerValue = x
        self.decimalValue = y

    def getBinaryString(self):
        return self.binaryValue
    def getIntegerValue(self):
        return self.integerValue
    def getDecimalValue(self):
        return self.decimalValue

    def convertToDecimal(self):
        # converts the binary string to a decimal value and returns it
        front_total = 0
        back_total = 0

        power_of_two_array = power_of_two(len(self.integerValue))
        decimal_array = decimal(len(self.decimalValue))

        for i in range(0, len(self.integerValue)):
            if self.integerValue[i] == '1':
                front_total = front_total + power_of_two_array[i]

        for c in range(0, len(self.decimalValue)):
            if self.decimalValue[c] == '1':
                back_total = back_total + decimal_array[c]

        output = front_total + back_total
        return str(output)

    def convertToHex(self):
        # converts the binary string to the hex equivalent
        general_array = []
        temp_array = []
        counter = -1
        for value in self.integerValue:
            if counter == 3:
                general_array.append(temp_array)
                counter = 0
                temp_array = []
                temp_array.append(value)
            else:
                temp_array.append(value)
                counter += 1

        general_array.append(temp_array)

        for i in range(0, len(general_array)):
            total = 0
            for x in range(len(base_array)-1, -1, -1):
                if general_array[i][x] == '1':
                    total = total + base_array[x]
            hexValue = hex_array[total][0]
            general_array[i] = hexValue

        general_array.append('.')

        # This is for the decimal part
        counter = 3
        total = 0
        for i in self.decimalValue:
            if i == '1':
                total = total + base_array[counter]
            counter = counter - 1
        hexValue = hex_array[total][0]
        general_array.append(hexValue)
        return str(''.join(general_array))

class hex:
    def __init__(self, data):
        self.hexValue = data
        state = False
        x = []
        y = []

        for i in data:
            if state==True:
                y.append(i)
            else:
                if i=='.':
                    state = True
                else:
                    x.append(i)
        self.integerValue = x
        self.decimalValue = y

    def getHexString(self):
        return self.hexValue
    def getIntegerValue(self):
        return self.integerValue
    def getDecimalValue(self):
        return self.decimalValue

    def convertToDecimal(self):
        a = positive_hex_array(len(self.integerValue))
        b = decimal_hex_array(len(self.decimalValue))

        front_total = 0
        back_total = 0

        for i in range(0, len(self.integerValue)):
            temp_state = False
            counter = 0
            while temp_state == False and counter <= len(hex_array):
                if hex_array[counter][0] == self.integerValue[i]:
                    front_total = front_total + (hex_array[counter][1] * a[i])
                    temp_state = True
                else:
                    counter += 1

        for i in range(0, len(self.decimalValue)):
            temp_state = False
            counter = 0
            while temp_state == False and counter <= len(hex_array):
                if hex_array[counter][0] == self.decimalValue[i]:
                    back_total = back_total + (hex_array[counter][1] * b[i])
                    temp_state = True
                else:
                    counter += 1

        mainTotal = front_total + back_total
        return str(mainTotal)

    def convertToBinary(self):
        # not finished
        print('N/A')


class decimal:
    def __init__(self, data):
        self.denaryValue = data
        state = False
        x = []
        y = []

        for i in data:
            if state==True:
                y.append(i)
            else:
                if i=='.':
                    state = True
                else:
                    x.append(i)
        self.integerValue = x
        self.decimalValue = y

    def getDecimalString(self):
        return self.denaryValue
    def getIntegerValue(self):
        return self.integerValue
    def getDecimalValue(self):
        return self.decimalValue

    def convertToHex(self):
        if self.decimalValue==[]:
            self.decimalValue = ['0']

        self.integerValue = int(''.join(x))
        self.decimalValue = float(''.join(y)) * 10**(-len(y))

        # for X
        temp_state = False
        integer_array = []
        decimal_state = []

        # gets remainders and puts them in the integer_array
        while temp_state == False:
            if self.integerValue == 0:
                temp_state = True
            else:
                remainder = self.integerValue % 16
                self.integerValue = self.integerValue // 16
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
        z = int(ceil(self.decimalValue * 16))
        decimal_value = hex_array[z][0]

        output = str(''.join(integer_array)) + str('.') + str(decimal_value)
        return str(output)

    def convertToBinary(self):
        integerPart = int(''.join(self.integerValue))
        decimalPart = float(''.join(self.decimalValue)) - 1

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

        return str(''.join(binary_array))
    
