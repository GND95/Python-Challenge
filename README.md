**Data Analysis in Python without 3rd party libraries.**
# PyBank
Created a Python script for analyzing financial records from a CSV file.</br>
Example of raw data from CSV:</br>
![PyBank Raw CSV Data](/PyBank/Images/1.png)<br/>
**The script calculates the following:**
* The total number of months included in the dataset
* The net total amount of "Profit/Losses" over the entire period
* The month-over-month changes in "Profit/Losses" over the entire period, then finds the average of those month-over-month changes
* The greatest increase in profits (date and amount) over the entire period
* The greatest decrease in profits (date and amount) over the entire period
* The script can both print to a terminal as well as export results to a file
</br>**Example of text output:**
<pre>Total Months: 86
Total: $38382578
Average Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)</pre> 
# PyPoll
Created a Python script for analyzing the votes for election/polling records from a 1 million+ row CSV file.</br>
Example of raw data from CSV:</br>
![PyPoll Raw CSV Data](/PyPoll/Images/1.png)<br/>
**The script calculates the following:**
* The total number of votes cast
* A complete list of candidates who received votes
* The percentage of votes each candidate won
* The total number of votes each candidate won
* The winner of the election based on popular vote
* The script can both print to a terminal as well as export results to a file
</br>**Example of text output:**
<pre>Khan: 63.0% (2218231)
Correy: 20.0% (704200)
Li: 14.0% (492940)
O'Tooley: 3.0% (105630)
-------------------------
Winner: Khan
-------------------------</pre> 
