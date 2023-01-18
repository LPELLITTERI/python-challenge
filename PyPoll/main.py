#import mods
import os
import csv

#Path to file
PyPoll_Path = os.path.join('election_data.csv')

#open csv

with open("PyPoll_Path", "r")as csvfile:
    
    csvreader = csv.reader(csvfile, delimiters = ',')
    
    #header
    header = next(csvfile)
    
    
    #Variables
    #sum of votes
    total_vote = {}
    #percentage won
    percent_won =  {}
    #total votes won by each candidate
    total_won = {}
    #list of candidates names
    candidate = (" Charles Casper Stockham","Diana DeGette","Raymon Anthony Doane")
    
    
    
    
    
    #loop thru data cadidate list
    for index_candidate in range(len(cadidate)):
        total_won = count(candidate)
        percent_won = 
    
    #count all votes 
    sum(total_vote)
    #name votes percent won / votes total number won list
    
    #calcultae winner list name 