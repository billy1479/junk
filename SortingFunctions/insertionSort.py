def insertionSort(myArray):
    # this loops through the array starting with the second element - it then compares this with the previous element and if it is less than
    # the previous element it swaps them
    # If the previous element is not less than (i.e. they are already in order), it moves to the element before that and compares them again - this repeats until y < 0
    # After this is moves onto the next element of the array and does the same process as above, moving through all the elements prior to it to see if it less than them
    for x in range(1, len(myArray)):
        current = myArray[x]
        y = x - 1
        while y >= 0 and current < myArray[y]:
            myArray[y+1] = myArray[y]
            y -= 1
        myArray[y+1] = current
    return myArray

x = [3,2,7,9,10]
print(insertionSort(x))

