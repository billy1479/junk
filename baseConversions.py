from code import interact


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
        return output

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