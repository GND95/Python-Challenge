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
    monthlyChange = [] #declaring empty list to keep track of the chance in profit/loss across each month

    for row in csvreader:#Read each row of data after the header
        monthlyValues.append(row[1]) #appending value of Profit/Loss column of the CSV to the monthlyValues list
        total += int((row[1])) #calculating total amount of profit/loss over the entire period
        #passing two values to CalculateChange function. the first parameter, startingValue, will be equal to the previous value of the iterator of the loop 
        #which would be the current position in the list monthlyValues - 1. the second parameter, endingValue, will be equal to the current value of the 
        # iterator of the loop. this value is then added to my empty list titled "monthlyChange"
        monthlyChange.append(CalculateChange(int(monthlyValues[rowCounter-1]), int(row[1])))
        #keeping track of the row count for two reasons: 1. to be able to get the proper index for my list 
        #and 2. to count the number of months of data (each month has its own row in the CSV) 
        rowCounter +=1 
    #calculating average by taking the sum of the list divided by the length of the list. subtracing one from the length because the value from the first iteration 
    #of the loop will be discarded since the value is zero as there is no prior value to calculate amount change to month one. rounding result to 2 decimal places.
    avgChange =  round(sum(monthlyChange) / (len(monthlyChange)-1),2) 
    maxIncrease = max(monthlyChange) #maximum value from the monthlyChange list
    minIncrease = min(monthlyChange) #minimum value from the monthlyChange list

    print(f"Total Months: {rowCounter}")
    print(f"Total: ${total}")
    print(f"Average Change: ${avgChange}")
    print(f"Greatest Increase in Profits: ${maxIncrease}")
    print(f"Greatest Decrease in Profits: ${minIncrease}")

    #export the results to a text file