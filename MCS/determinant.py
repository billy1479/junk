# finds the determinant of a matrix (either 2x2 or 3x3)
dimension = input('Please enter what dimension the matrix is: 2x2 or 3x3 (Please enter 2 or 3)')
if dimension == 2:
    print('---                  ---')
    print('This will calculate the derminant of the 2x2 matrix you are about to enter')
    print('---                  ---')
    print('You will input values from left to right and then onto the next row.')
    matrix2 = ['-','-','-','-']
    for x in range(0,3):
        if x == 2:
            print('This is for the second row.')
        element = int(input('Please enter in the element:   '))
        matrix2[x] = element
    determinant = matrix2[0]*matrix2[3] - matrix2[1]*matrix2[2]
    print('The determinant for this matrix is - ' + str(determinant))

elif dimension == 3:
    print('---                  ---')
    print('This will calculate the derminant of the 3x3 matrix you are about to enter')
    print('---                  ---')
    print('You will input values from left to right and then onto the next row.')
    matrix3 = ['-','-','-','-','-','-','-','-','-']
    for x in range(0, 8):
        if x == 3:
            print('This is for the second row.')
        elif x == 6:
            print('This is for the third row.')
        element = int(input('Please enter in the element:   '))
        matrix3[x] = element
    determinant = (matrix3[0]*(matrix3[4]*matrix3[8] - matrix3[1]*matrix3[2])) - (matrix3[1]*(matrix3[3]*matrix3[8]-matrix3[5]*matrix3[6]) + (matrix3[2]*(matrix3[3]*matrix3[7] - matrix3[4]*matrix3[6])))
    print('The determinant for this matrix is - ' + str(determinant))
else:
    print('Please enter the right dimension. ')

