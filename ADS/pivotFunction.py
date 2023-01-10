# from ads coursework

def pivot(L):
    import random
    randomNumber = []
    counter = 0
    while counter < 5:
        x = random.randint(0, len(L) - 1)
        if x in randomNumber:
            pass
        else:
            randomNumber.append(x)
            counter += 1

    newArray = []
    for y in randomNumber:
        newArray.append(L[y])

    sortedList = selectionSort(newArray)
    print(sortedList)
    return sortedList[2]


def selectionSort(L):
    for x in range(0, len(L) - 1):
        min = x
        for y in range(x + 1, len(L)):
            if L[y] < L[min]:
                min = y
        z = L[x]
        L[x] = L[min]
        L[min] = z
    return L


print(pivot([5,2,3,8,9,10,6,7]))

    