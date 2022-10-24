from dataclasses import dataclass


class Hash:
    def __init__(self, length):
        self.hashTable = dict.fromkeys((range(length)))
        self.size = length

    def insertIntoTable(self, data):
        if type(data) == str:
            total = 0
            
        elif type(data) == int:

        elif type(data) == float:

