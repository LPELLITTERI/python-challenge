import os
import csv

#Path to file
file = os.path.join('election_data.csv')

#open csv
with open(file, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #header
    header = next(csvreader)
    
    #Variables
    voter_ids = []
    candidate_votes = {}
    total_votes = 0
    
    #count all votes 
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1 
        else: 
            candidate_votes[candidate] = 1
    
    #calculate percentage of votes won by each candidate
    for candidate, votes in candidate_votes.items():
        percent_won = (votes / total_votes) * 100
        candidate_votes[candidate] = (votes, percent_won)
        
    #calculate winner
    winner = max(candidate_votes, key=lambda k: candidate_votes[k][0])
    
    #print results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate, (votes, percent) in candidate_votes.items():
        print(f"{candidate}: {percent:.3f}% ({votes})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")
    
    #Export to TXT
    with open("output.txt", "w") as text_file:
        text_file.write("Election Results\n")
        text_file.write("-------------------------\n")
        text_file.write(f"Total Votes: {total_votes}\n")
        text_file.write("-------------------------\n")
        for candidate, (votes, percent) in candidate_votes.items():
            text_file.write(f"{candidate}: {percent:.3f}% ({votes})\n")
        text_file.write("-------------------------\n")
        text_file.write(f"Winner: {winner}\n")
        text_file.write("-------------------------\n")
