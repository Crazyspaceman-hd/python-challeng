#Import .csv
import os
import csv
months=0
net=0

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        # total number of months
        months=months+1
        # net total profit/loss
        net= net + int(row[1])
        


# average of changes in profit/loss
# greatest profits date and amount
# greatest loss date and amount