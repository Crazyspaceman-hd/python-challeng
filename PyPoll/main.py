#Import .csv
import os
import csv
votes = []
final_votes = []
percentage = []
results ={}

csvpath = os.path.join("Resources", "election_data.csv")


#percentage of votes for each candidate

#winner of the election
#loop through list seperating votes into list
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        votes.append(row[2])
#store total number of votes in seperate variable
votes_total= len(votes)

#create list of candidate names        
candidates=set(votes)
for name in candidates:
    final_votes.append (votes.count(name))
    # percentage.append(round(votes.count(name)/votes_total, 3))
   #number of votes for each candidate
#total number of votes cast
    results[name] = votes.count(name)

print(votes_total)

for p, v in results.items():
    print(f'{p}: {round((v/votes_total)*100, 5)}% ({v}) ')
# print(results)
#print(candidates)
#print(percentage)

        
#print (candidates)