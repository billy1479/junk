def insertionSort(myArray):
    for x in range(1, len(myArray)):
        current = myArray[x]
        y = x - 1
        while y >= 0 and current < myArray[y]:
            myArray[y+1] = myArray[y]
            y -= 1
        myArray[y+1] = current
    return myArray



