#Import .csv
import os
import csv
months=0
net=0
before=0
change_tote=0
prof_max=0
prof_min=0



budget = os.path.join("Resources", "budget_data.csv")

with open(budget, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        if before == 0:
            before=int(row[1])
        print (before)
        # total number of months
        months=months+1
        # net total profit/loss
        net= net + int(row[1])
        # average of changes in profit/loss
        change= int(row[1])-before       
        before=int(row[1])
        change_tote=change_tote+change
        # greatest profits date and amount
        if change > prof_max:
            prof_max= change
            date_prof_max= row[0]
        # greatest loss date and amount
        if change < prof_min:
            prof_min= change
            date_prof_min= row[0]
        print (change)

       
    change_avg=round(change_tote/(months-1), 2)
    
print("Financial Analysis")
print("-------------------------------")
print("Total Months: " + str(months))
print("Total: $"+ str(net))
print("Average Change: $"+ str(change_avg))
print("Greatest Increase in Profits: "+ date_prof_max +" ($"+str(prof_max) + ")")
print("Greatest Decrease in Profits: "+ date_prof_min +" ($"+str(prof_min) + ")")

with open('Financial_Analysis.txt', 'w') as f:
    print('Financial Analysis', file=f)
    print("-------------------------------", file=f)
    print("Total Months: " + str(months), file=f)
    print("Total: $"+ str(net), file=f)
    print("Average Change: $"+ str(change_avg), file=f)
    print("Greatest Increase in Profits: "+ date_prof_max +" ($"+str(prof_max) + ")", file=f)
    print("Greatest Decrease in Profits: "+ date_prof_min +" ($"+str(prof_min) + ")", file=f)