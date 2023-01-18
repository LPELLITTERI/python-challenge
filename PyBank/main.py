#Import mods
import os
import csv




#Path to file 
PyBank_Path = os.path.join('budget_data.csv')


#Open CSV
with open('PyBank_Path', "r")as csvfile:
    
    
    budget_csv = csv.reader(csv.file, delimiter= ',')
csvreader = csv.reader(csvfile,delimiter = ",")   

#Header
header = next(csvfile)  


#Variables to store data 
time_months = []
profit_losses = []
total_net= []
change_in_loss = []
greatest_profit_increase = []
greatest_profit_decrease = []
max_month = []
index_min = []
index_max = []
   
#Loop
for row in budget_csv:
    #date
    time_months.append(row[0])
    
    #Profit/Loss
    profit_losses.append(float(row[1]))
    
    


#Date #The total number of months included in the dataset var1
time_months = (len("months"))

#The net total amount of "Profit/Losses" over the entire period var3
total_net = sum("Profit/Loss")



#The changes in "Profit/Losses" average over month
change_in_loss = total_net / time_months

#The greatest increase in profits (date and amount)  var 5

greatest_profit_increase = max(greatest_profit_decrease)

#Index of increase to find the date 
index_greatest_increase = greatest_profit_decrease.index("max_profit_decrease")
max_month = time_months[index_max]



#The greatest decrease in profits (date and amount) over the entire period var6
min_profits = min("profits_losses")


#Using the index of the greatest decrease to find the date
index_min = "profits_losses".index(min_profits)
min_months = time_months[index_min]










 









