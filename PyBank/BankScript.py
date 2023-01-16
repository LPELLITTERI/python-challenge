import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with  open(csvpath) as csv_file:
    csv_reader = csv.reader(csv.file, delimiter= ',')
    
    
csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

   

#for row in csv.reader:
   # Date = row[0]
    #Profit_Losses = row[1]

#Date = len(row[0])





#time_months = []
#profit_losses = []
#total_loss = []
#change_in_loss = []
#greatest_profit_increase_date_amount = []
#greatest_profit_decrease_date_amount = []


#The total number of months included in the dataset var1

#time_months = len(Date)
#print(time_months)

#The net total amount of "Profit/Losses" over the entire period var3

#The changes in "Profit/Losses" over the entire period, and then the average of those changes var4

#The greatest increase in profits (date and amount) over the entire period var 5

#The greatest decrease in profits (date and amount) over the entire period var6



#with open(PyBank_path) as csvfile:
    #csv_reader = csv.reader(csvfile, delimiter=',')


#header = next(csv_reader)

#for row in csv_reader:
   # Date = row[0]
    #Profit_Losses = row[1]









 









