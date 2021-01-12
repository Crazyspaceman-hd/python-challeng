#Import .csv
import os
import csv
#declare lists and dictionaries
votes = []
final_votes = []
percentage = []
results ={}

#create path to CSV file
csvpath = os.path.join("Resources", "election_data.csv")

#loop through CSV seperating votes into list
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

#print summary
print("Election Results")
print("---------------------------")
print("Total Votes: ", votes_total)
print("---------------------------")
#loop through candidate:votes dictionary printing results
for p, v in results.items():
    #print candidates name, set format and calculate percent of vote received, print number of candidate votes
    print(f'{p}:  {"{:.3%}".format(v/votes_total)} ({v}) ')
print("---------------------------")
#determine winner from results dictionary and print
print (f'Winner:  {max(results, key=results.get)}')
print("---------------------------")

#send summary to text file
with open('./Analysis/Election_results.txt', 'w') as f:
     print("Election Results", file=f)
     print("---------------------------", file=f)
     print("Total Votes: ", votes_total, file=f)
     print("---------------------------", file=f)
     for p, v in results.items():
        print(f'{p}:  {"{:.3%}".format(v/votes_total)} ({v}) ', file=f)
     print("---------------------------", file=f)
     print (f'Winner:  {max(results, key=results.get)}', file=f)
     print("---------------------------", file=f)