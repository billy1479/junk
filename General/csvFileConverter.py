# This has a specific use for a seperate project of my own
import csv as csv
postcode_array = []
with open('postcodes.csv', 'r') as csvfile:
    counter = 1
    for row in csvfile:
        postcode = []
        row = row.split(',')
        postcode.append(row[2])
        postcode.append(row[3])
        myPostCode = ' '.join(postcode)
        x = [counter, myPostCode, '',row[4]]   
        postcode_array.append(x)
        counter = counter + 1

print(postcode_array)

counter = 0
with open('newPostcodes.csv', 'w') as newCSV:
    csvwriter = csv.writer(newCSV)
    for x in range(0, len(postcode_array)):
        csvwriter.writerow(postcode_array[x])


