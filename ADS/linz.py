import random
# numArray = [0,1,2,3,4,5,6,7]
# linzArray = []
# testArray = []
# def linz_ordering_eight():
#     global numArray
#     global testArray
#     if len(linzArray) == 8:
#         return linzArray
#     else:
#         if len(linzArray) > 1:
#             if len(numArray) == 0:
#                 print('Number array has been restored')
#                 value = linzArray.pop()
#                 print('Popped value is ' + str(value))
#                 numArray = [0,1,2,3,4,5,6,7]
#                 for x in linzArray:
#                     if x in numArray:
#                         numArray.remove(x)
#                 testArray = []
#                 return linz_ordering_eight()
#             else:
#                 x = random.randint(0,len(numArray) - 1)
#                 value = numArray[x]
#                 y = ((linzArray[len(linzArray) - 1]) - value) % 8
#                 if y in testArray:
#                     numArray.remove(value)
#                     return linz_ordering_eight()
#                 else:
#                     print(linzArray)
#                     numArray.remove(value)
#                     testArray.append(y)
#                     linzArray.append(value)
#                     return linz_ordering_eight()
#         else:
#             x = random.randint(0,len(numArray) - 1)
#             value = numArray[x]
#             numArray.remove(value)
#             linzArray.append(value)
#             return linz_ordering_eight()

def linz_ordering_eight2():
    global numArray
    global testArray
    global linzArray
    testArray = []
    linzArray = []
    numArray = [0,1,2,3,4,5,6,7]
    def myFunction():
        global numArray
        global testArray
        global linzArray
        if len(linzArray) == 8:
            return linzArray
        else:
            if len(linzArray) > 1:
                if len(numArray) == 0:
                    print('Number array has been restored')
                    value = linzArray.pop()
                    print('Popped value is ' + str(value))
                    numArray = [0,1,2,3,4,5,6,7]
                    for x in linzArray:
                        if x in numArray:
                            numArray.remove(x)
                    testArray = []
                    return myFunction()
                else:
                    x = random.randint(0,len(numArray) - 1)
                    value = numArray[x]
                    y = ((linzArray[len(linzArray) - 1]) - value) % 8
                    if y in testArray:
                        numArray.remove(value)
                        return myFunction()
                    else:
                        print(linzArray)
                        numArray.remove(value)
                        testArray.append(y)
                        linzArray.append(value)
                        return myFunction()
            else:
                x = random.randint(0,len(numArray) - 1)
                value = numArray[x]
                numArray.remove(value)
                linzArray.append(value)
                return myFunction()
    return myFunction()

print(linz_ordering_eight2())


