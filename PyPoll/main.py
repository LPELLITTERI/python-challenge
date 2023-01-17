#import mods
import os
import csv

#Path to file
csvfile = os.path.join('election_data.csv')

#open csv

with open("election_data.csv", "r")as csvfile:
    
    csvreader = csv.reader(csvfile, delimiters = ',')
    
    #header
    header = next(csvfile)
    
    
    #Variables
    total_vote = {}
    percent_won =  {}
    total_won = {}
    candidate = ("")
    
    
    
    
    
    #loop thru data cadidate list
    for 
    
    #count all votes 
    
    #name votes percent won / votes total number won list
    
    #calcultae winner list name 