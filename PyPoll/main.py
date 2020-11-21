import os, csv

filePath = os.path.join('Resources', 'election_data.csv')#import csv block of code
with open(filePath) as csvfile:#open the path to the CSV file as a new object
    csvreader = csv.reader(csvfile, delimiter=',') #pass the csvfile object to a new variable, csvreader
    csv_header = next(csvreader) #skipping the header so we get the correct count of rows
    initialCandidateList = ["Khan", "Correy", "Li", "O'Tooley"] #populating list with the initial known candidates
    candidates = { initialCandidateList[0]:0, initialCandidateList[1]:0, initialCandidateList[2]:0, initialCandidateList[3]:0 } #storing the list of candidate names in a dictionary so I can map vote count to candidate
    rowCounter = 0

    for row in csvreader:#Read each row of data after the header
        rowCounter+=1 #keep track of number of rows since each row is a vote
        #if the candidate is not already in initialCandidateList (is a candidate which has not recieved a vote yet) then append this candidate to the list
        if row[2] not in initialCandidateList:
            initialCandidateList.append(row[2])
        if row[2] == initialCandidateList[0]:
            candidates[initialCandidateList[0]]+=1
        elif row[2] == initialCandidateList[1]:
            candidates[initialCandidateList[1]]+=1
        elif row[2] == initialCandidateList[2]:
            candidates[initialCandidateList[2]]+=1
        elif row[2] == initialCandidateList[3]:
            candidates[initialCandidateList[3]]+=1

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {rowCounter}") #each row is a vote so row count is equal to the number of votes
    print("-------------------------")
    print (candidates)

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