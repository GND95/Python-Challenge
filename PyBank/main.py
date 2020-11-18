import os, csv

def CalculateChange(startingValue, endingValue):
    return (endingValue - startingValue) #calculating the difference between the ending value and the starting value

filePath = os.path.join('Resources', 'budget_data.csv')#import csv block of code
with open(filePath) as csvfile: #open the path to the CSV file as a new object
    csvreader = csv.reader(csvfile, delimiter=',') #pass the csvfile object to a new variable, csvreader
    csv_header = next(csvreader) #skipping the header so we get the correct count of rows
    print("Financial Analysis")
    print("----------------------------")
    rowCounter, total, avgChange, maxIncrease, minIncrease = 0, 0, 0, 0, 0
    monthlyValues = [] #declaring empty list to keep track of individual monthly profit/loss values from the CSV

    for row in csvreader:#Read each row of data after the header
        monthlyValues.append(row[1]) #appending value of Profit/Loss column of the CSV to the monthlyValues list
        total += int((row[1])) #calculating total amount of profit/loss over the entire period
        #passing two values to CalculateChange function. the first parameter, startingValue, will be equal to the previous value of the iterator of the loop 
        #which would be the current position in the list monthlyValues - 1. the second parameter, endingValue, will be equal to the current value of the iterator of the loop
        print(CalculateChange(int(monthlyValues[rowCounter-1]), int(row[1])))
        rowCounter +=1 #keeping track of the row count for two reasons: 1. to be able to get the proper index from my list and 2. to count the number of months of data (each month has its own row in the CSV) 

    print(f"Total Months: {rowCounter}")
    print(f"Total: ${total}")
    print(f"Average Change: ")
    print(f"Greatest Increase in Profits ")
    print(f"Greatest Decrease in Profits ")