# attempt 1
# this works but need to sort out issue with recursion maxing out because the random numbers keep repeating

import random
numArray = [0,1,2,3,4,5,6,7]
linzArray = []
testArray = []


def linz_ordering_eight():
    global numArray
    global testArray
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
                return linz_ordering_eight()
            else:
                x = random.randint(0,len(numArray) - 1)
                value = numArray[x]
                y = ((linzArray[len(linzArray) - 1]) - value) % 8
                if y in testArray:
                    numArray.remove(value)
                    return linz_ordering_eight()
                else:
                    print(linzArray)
                    numArray.remove(value)
                    testArray.append(y)
                    linzArray.append(value)
                    return linz_ordering_eight()
        else:
            x = random.randint(0,len(numArray) - 1)
            value = numArray[x]
            numArray.remove(value)
            linzArray.append(value)
            return linz_ordering_eight()


# def mainFunction():
#     numArray = [0,1,2,3,4,5,6,7]
#     linzArray = []
#     testArray = []
#     def linz_ordering_eight():
#         print('this has run')
#         print(linzArray)
#         print(testArray)
#         print(numArray)
#         if len(linzArray) == 8:
#             return linzArray
#         else:
#             if len(linzArray) > 1:
#                 if len(numArray) == 0:
#                     numArray = [0,1,2,3,4,5,6,7]
#                 else:
#                     x = random.randint(0,len(numArray) - 1)
#                     value = numArray[x]
#                     y = ((linzArray[len(linzArray) - 1]) - value) % len(linzArray)
#                     if y in testArray or y == 0:
#                         numArray.remove(value)
#                         return linz_ordering_eight()
#                     else:
#                         numArray.remove(value)
#                         testArray.append(y)
#                         linzArray.append(value)
#                         return linz_ordering_eight()
#             else:
#                 x = random.randint(0,len(numArray) - 1)
#                 value = numArray[x]
#                 numArray.remove(value)
#                 linzArray.append(value)
#                 return linz_ordering_eight()
#     linz_ordering_eight()

# print(mainFunction())





# def linz_ordering_eight():
#     if len(linzArray) == 8:
#         return linzArray
#     else:
#         if len(linzArray) > 1:
#             if len(usedArray) == len(numArray):
#                 linzArray.pop(len(linzArray) - 1)
#                 usedArray = []
#             else:
#                 x = random.randint(0,len(numArray) - 1)
#                 value = numArray[x]
#                 y = ((linzArray[len(linzArray) - 1]) - value) % len(linzArray)
#                 if y in testArray or y == 0:
#                     numArray.remove(value)
#                     usedArray.append(value)
#                     return linz_ordering_eight()
#                 else:
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
            
            





print(linz_ordering_eight())


