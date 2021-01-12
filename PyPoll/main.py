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
#create dictionary of candidates names and vote counts
for name in candidates:
    final_votes.append (votes.count(name))
    results[name] = votes.count(name)

print(votes_total)

for p, v in results.items():
    print(f'{p}:  {round((v/votes_total)*100, 3)}% ({v}) ')
# print(results)
#print(candidates)
#print(percentage)
print (max(results, key=results.get))
        
#print (candidates)