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

print(selectionSort([5,2,3,7,1,4]))