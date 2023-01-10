# attempt 1
# this works but need to sort out issue with recursion maxing out because the random numbers keep repeating
import random
numArray = [0,1,2,3,4,5,6,7]
linzArray = []
testArray = []

def linz_ordering_eight():
    if len(linzArray) == 8:
        return linzArray
    else:
        if len(linzArray) > 1:
            print(numArray2)
            x = random.randint(0,len(numArray2) - 1)
            value = numArray2[x]
            y = ((linzArray[len(linzArray) - 1]) - value) % len(linzArray)
            if y in testArray:
                numArray2.remove(value)
                return linz_ordering_eight()
            else:
                numArray.remove(value)
                numArray2 = numArray[:]
                testArray.append(y)
                linzArray.append(value)
                return linz_ordering_eight()
        else:
            x = random.randint(0,len(numArray) - 1)
            value = numArray[x]
            numArray.remove(value)
            # numArray2.remove(value)
            linzArray.append(value)
            return linz_ordering_eight()

print(linz_ordering_eight())

# -------------- end of attempt 1 ------------------------------

