#Import the modules
import os
import csv
#Declare variables
months=0
net=0
before=0
change_tote=0
prof_max=0
prof_min=0

#route to CSV
budget = os.path.join("Resources", "budget_data.csv")

#Open the CSV
with open(budget, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #Skip header row
    csv_header = next(csvreader)
    #Loop
    for row in csvreader:
        #reset variable involved in profit/loss calculations to fix error with change total
        if before == 0:
            before=int(row[1])
        # total number of months
        months=months+1
        # net total profit/loss
        net= net + int(row[1])
        # average of changes in profit/loss
        change= int(row[1])-before
        #pull value for next iterations change calculation       
        before=int(row[1])
        #add iterations change to change total
        change_tote=change_tote+change
        #check if change is higher than all previous changes, if so save change value and date
        if change > prof_max:
            prof_max= change
            date_prof_max= row[0]
        #check if change is lower than all previous changes, if so save change value and date
        if change < prof_min:
            prof_min= change
            date_prof_min= row[0]
    #calculate change average by dividing total by number of months minus one 
        # the subtraction is neccessary because the profit/loss changed one less time than the number of months
    change_avg=round(change_tote/(months-1), 2)

#print summary
print("Financial Analysis")
print("-------------------------------")
print("Total Months: " + str(months))
print("Total: $"+ str(net))
print("Average Change: $"+ str(change_avg))
print("Greatest Increase in Profits: "+ date_prof_max +" ($"+str(prof_max) + ")")
print("Greatest Decrease in Profits: "+ date_prof_min +" ($"+str(prof_min) + ")")

#export summary to text file.
with open('./Analysis/Financial_Analysis.txt', 'w') as f:
    print('Financial Analysis', file=f)
    print("-------------------------------", file=f)
    print("Total Months: " + str(months), file=f)
    print("Total: $"+ str(net), file=f)
    print("Average Change: $"+ str(change_avg), file=f)
    print("Greatest Increase in Profits: "+ date_prof_max +" ($"+str(prof_max) + ")", file=f)
    print("Greatest Decrease in Profits: "+ date_prof_min +" ($"+str(prof_min) + ")", file=f)