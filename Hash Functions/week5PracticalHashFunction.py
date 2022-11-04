def hash(d):
    """given a list d of integers returns a list of length 13
    describing the hash table obtained when the hash function
    h(k)=k mod 13 is applied to each integer k in d"""
    #initialize table
    table = ["-"]*13
    #
    for x in d:
        position = x % 13
        if table[position] == '-':
            table[position] = x
        elif table[position] == x:
            pass
        else:
            counter = 0
            positionFound = False
            while positionFound == False and counter != 12:
                position = (position+1) % 13
                counter += 1
                if table[position] == '-':
                    table[position] = x
                    positionFound = True
                elif table[position] == x:
                    positionFound = True
    return table
    
def testq3():
    assert hash([25,6,39,17,12,15,53]) == [39, 12, 15, 53, 17, '-', 6, '-', '-', '-', '-', '-', 25]
    assert hash([0,1,2,3,4,5,6,7,8,9,10,11,12]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert hash([10,11,12,0,1,2,3,4,5,6,7,8,9]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert hash([-1,-2,-3]) == ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', -3, -2, -1]
    assert hash([53,25,6,39,17,12,15]) == [39, 53, 12, 15, 17, '-', 6, '-', '-', '-', '-', '-', 25]
    print ("all basic tests passed")
    assert hash([25,6,39,17,12,15,53,53]) == [39, 12, 15, 53, 17, '-', 6, '-', '-', '-', '-', '-', 25]
    assert hash([1,1,1,1,2,2,2,3,3,3]) == ['-', 1, 2, 3, '-', '-', '-', '-', '-', '-', '-', '-', '-']    
    print ("all tests involving duplicates passed")
    print ("now  we test inputs containing more integers than the size of the table")
    print ("you will wait forever if you have not considered this case")
    assert hash([0,1,2,3,4,5,6,7,8,9,10,11,12,13]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert hash([0,1,1,1,7,1,2,3,4,0,5,6,7,8,9,9,9,10,11,12,13]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print ("all tests passed")
    