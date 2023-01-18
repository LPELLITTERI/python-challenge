#import mods
import os
import csv

#Path to file
file = os.path.join('election_data.csv')

#open csv

with open("file", "r")as csvfile:
    
    csvreader = csv.reader(csvfile, delimiters = ',')
    
    #header
    header = next(csvreader)
    
    
    #Variables
    voter_ids = []
    candidates = {}
    
    #sum of votes
    total_vote = {}
    #percentage won
    percent_won =  {}
    #total votes won by each candidate
    total_won = {}
    #list of candidates names
    candidate = []
    
    
    #loop thru list names 
    for row in csvreader:
        if row[2] not in candidates:
            candidates.append(row[2])
            
            print(candidate)
        

    for key, value in candidates.items():
        print(key, value)
    
   # count all votes 
    for row in csvreader:
        candidates = row [2]
        
        if candidates in candidate:
            candidates[candidates]+= 1 
            
        else: 
            candidates[candidate] = 1 
            print(candidates)
        
   
    #name votes percent won / votes total number won list
    percentage = int("canditates"/len(candidate.items))*100
 
print(percent_won, '% of ')
    
    #calculate winner list name 
    
    