import os, csv

filePath = os.path.join('Resources', 'election_data.csv')#import csv block of code
with open(filePath) as csvfile: #open the path to the CSV file as a new object
    csvreader = csv.reader(csvfile, delimiter=',') #pass the csvfile object to a new variable, csvreader
    csv_header = next(csvreader) #skipping the header so we get the correct count of rows
    print("Election Results")
    print("-------------------------")
    #count number of rows in csv without storing entire csv file in memory to allow for faster execution. since each row is an entry for a vote, number of rows = total votes
    print("Total Votes: " + str(sum(1 for line in csvfile)))
    print("-------------------------")

    candidates = { "Khan":0, "Correy":0, "Li":0, "O'Tooley":0 }


    #may use this section of code later
    # for row in csvreader:#Read each row of data after the header
    #     monthlyValues.append(row[2]) 


#I will reuse this function when I am closer to being done with the code
# def GenerateResults(resultType):#function to print the results to terminal or export the results to a text file
#     if (resultType == "print"):#print results to terminal
#         print(f"")
#     elif(resultType == "file"):#export the same information to a text file
#         output_path = os.path.join("output", "pollResults.txt")
#         with open(output_path, 'w') as txtFile:
#             txtFile.write(f"")

# GenerateResults("print")
# GenerateResults("file")