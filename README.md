# Python Challenge
## PyBank
The script imports the CSV file and then runs it through a loop. It stores very little data instead checking and replacing variables inside the loop and adding to totaling variables. There are 3 'if' statements within the loop, one of which is there to correct an issue with the first pass that affects the average profit/loss change. The other 'if' statements are there to check if there has been a change in the maximum profit or loss and to store the change value and associated month

Outside of the loop the average of the change between each months profit/loss is calculated using the 'months' variable which has been iterating through the loop. Finally there are 2 sections of print statements summarizing the work done to the data. The first of these sections prints to the terminal and the second prints to text file named "Financial_Analysis.txt"

## PyPol
The script imports the CSV file and runs it through a loop seperating the names which have been voted for and storing them in a list. The length of this list is then taken to determine the total number of votes, a set function is then used to to determine the name of each candidate which has been voted for and store them in a list. The candidates list is then run through a loop where the number of votes for them are counted and stored in a dictionary(results) paired with the name of the candidate.

There are then 2 sections of print statements to provide an analysis of the data. Inside these sections is a loop that runs through the results dictionary retreiving the candidates names and the number of votes received. The print statement in this loop contains code to calculate and fotmat the percentage of the vote received by each candidate. Finally there is a print statement which uses the max function on the results dictionary to determine and print the winner. The second section of print statements is the same but prints to a text file instead of the terminal.
