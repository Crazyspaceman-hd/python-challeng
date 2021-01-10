#Import .csv
import os
import csv
months=0
net=0
before=0
change_tote=0
prof_max=0
prof_min=0



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
        change= int(row[1])-before
        before=int(row[1])
        change_tote=change_tote+change
        # greatest profits date and amount
        if change > prof_max:
            prof_max= change
            date_prof_max= row[0]
        if change < prof_min:
            prof_min= change
            date_prof_min= row[0]
        

       
    change_avg=round(change_tote/months, 2)
    
print("Financial Analysis")
print("-------------------------------")
print("Total Months: " + str(months))
print("Total: $"+ str(net))
print("Average Change: $"+ str(change_avg))
print("Greatest Increase in Profits: "+ date_prof_max +" $"+str(prof_max))
print("Greatest Decrease in Profits: "+ date_prof_min +" $"+str(prof_min))
    

        



        



# greatest profits date and amount
# greatest loss date and amount