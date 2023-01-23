#Import mods
import os
import csv

#Path to file 
PyBank_Path = os.path.join('budget_data.csv')
#output
analysis_path = os.path.join('Analysis.txt')

#Variables to store data 
time_months = []
profit_losses = []
total_net= []
change_in_loss = []
greatest_profit_increase = ["", 0 ]
greatest_profit_decrease = ["", 0 ]
max_month = []
index_min = []
index_max = []

#Open CSV
with open(PyBank_Path, "r")as csvfile:
    
    budget_csv = csv.reader(csvfile, delimiter= ',')


    #Header
    header = next(budget_csv)  


    # #Variables to store data 
    # time_months = []
    # profit_losses = []
    # total_net= []
    # change_in_loss = []
    # greatest_profit_increase = []
    # greatest_profit_decrease = []
    # max_month = []
    # index_min = []
    # index_max = []
   
    #Loop
    for row in budget_csv:
        #date
        time_months.append(row[0])
        
        #Profit/Loss
        profit_losses.append(float(row[1]))
        
        


    #Date #The total number of months included in the dataset var1
    time_months = (len(time_months))

    #The net total amount of "Profit/Losses" over the entire period var3
    total_net = sum(profit_losses)



    #The changes in "Profit/Losses" average over month
    change_in_loss = total_net / time_months

    #The greatest increase in profits (date and amount)  var 5

    #max_profit_decrease = max(greatest_profit_decrease[1])

    #Index of increase to find the date 
    #index_greatest_increase = greatest_profit_decrease.index(max_profit_decrease)
    #max_month = time_months[index_max]



    #The greatest decrease in profits (date and amount) over the entire period var6
    # min_profits = min(profits_losses)


    #Using the index of the greatest decrease to find the date
    
#create output report
output_report = (
    f"Financial Analysis\n"
    f"------------------\n"
    f"Total Months: {time_months}\n"
    f"Total Net: {total_net}\n"
    
)

#print output report
print(output_report)

#export to TXT file
with open(analysis_path, "w") as report_txt:
    report_txt.write(output_report)






 









