def highScoreInsertion(H, E):
    arrayLength = 9 # where the length is 10 but we are indexing from 0
    myState = False
    counter = 0
    while myState == False:
        if E[0] > H[counter][0]:
            # This loops through the rest of the array and moves the values up by 1 to make room for the new element
            if H[9] == 'NULL':
                # This shifts all the values up by 1 and makes room for the new element
                for x in range(8, counter - 1, -1):
                    H[x+1] = H[x]
                H[counter] = E
            else:
                # This stores the value being removed at the end of the list for it to be outputted to the user to show that it has been removed
                deletedValue = H[9]
                print('Sorry - ' + str(deletedValue) + ' has had their highscore removed')
                H[9] = 'Null'
                for x in range(8, counter - 1, -1):
                    H[x+1] = H[x]
                H[counter] = E
            myState = True
        else:
            # This stores the next value in the array as value and increments the counter to point to the next value
            value = H[counter][0]
            counter = counter + 1
    return H

mainArray = [[940,'Mike'],[880,'Rob'],[830,'Jill'],[790,'Paul'],[750,'Anna'],[660,'Rose'],[650,'Jack'],'NULL','NULL','NULL']
newAddition = [900, 'Billy']
print(mainArray)
print(highScoreInsertion(mainArray, newAddition))