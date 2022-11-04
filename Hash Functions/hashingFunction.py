# only works with strings
# step value is incremeneted by 1 - needs to be changed if size increase drastically
# check one note for methods of skip
class Hash:
    def __init__(self, length):
        # sets up a dictionary of length - length
        self.hashTable = dict.fromkeys((range(length)))
        self.size = length

    def insertIntoTable(self, data):
        # data gets inserted into the table with a skip value of + 1 - this needs to be changed to one of the new methods studied
        total = 0
        for x in data:
            total = total + ord(x)
        value = (total * 2) % self.size
        state = False
        while state == False:
            if self.hashTable[value] != 'None':
                self.hashTable[value] = data
                state = True
            else:
                value += 1
        
    def displayHashTable(self):
        # prints all the values in the dictionary
        for x in range(0, self.size):
            print(str(x) + ' : ' + str(self.hashTable[x]))

    def searchTable(self, data):
        # searches for a value in the table - will need to be changed if the skip value changes
        total = 0
        for x in data:
            total = total + ord(x)
        value = (total * 2) % self.size
        if self.hashTable[value] == data:
            print('This value exists.')
        else: 
            print('This value does not exist')

    def deleteValue(self, data):
        # this searches for a value and deletes it if it exists - needs to be changed if skip value changes
        total = 0
        totalCounter = 0
        for x in data:
            total = total + ord(x)
        value = (total * 2) % (self.size)
        found = False
        while found == False and totalCounter != self.size:
            value = value % self.size
            if self.hashTable[value] == data:
                self.hashTable[value] = 'None'
                found = True
                print('This has been deleted')
            else:
                value += 1
                totalCounter += 1
        
        if found == False:
            print('The value does not exist')
        else:
            print('The value has been deleted')

