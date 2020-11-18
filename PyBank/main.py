import os, csv

#import csv
filePath = os.path.join('Resources', 'budget_data.csv')
with open(filePath) as csvfile: #open the path to the CSV file as a new object
    csvreader = csv.reader(csvfile, delimiter=',') #pass the csvfile object to a new variable, csvreader    
    csv_header = next(csvreader)
    print(csv_header)

    for row in csvreader:#Read each row of data after the header
        print(row)
