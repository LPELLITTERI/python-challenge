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
total_net = 0
change_in_loss = 0
greatest_profit_increase = ["", 0]
greatest_profit_decrease = ["", 9999999]
max_month = ""
index_min = 0
index_max = 0
min_profits = 0

#Open CSV
with open(PyBank_Path, "r") as csvfile:
    
    budget_csv = csv.reader(csvfile, delimiter=',')

    #Header
    header = next(budget_csv)  

    #Loop
    for row in budget_csv:
        #date
        time_months.append(row[0])
        
        #Profit/Loss
        profit_losses.append(float(row[1]))
        
        #Total Net
        total_net += float(row[1])

        #Greatest Increase
        if float(row[1]) > greatest_profit_increase[1]:
            greatest_profit_increase[1] = float(row[1])
            greatest_profit_increase[0] = row[0]
            index_max = len(time_months) - 1

        #Greatest Decrease
        if float(row[1]) < greatest_profit_decrease[1]:
            greatest_profit_decrease[1] = float(row[1])
            greatest_profit_decrease[0] = row[0]
            index_min = len(time_months) - 1

    #Date #The total number of months included in the dataset
    num_months = len(time_months)

    #The changes in "Profit/Losses" average over month
    change_in_loss = total_net / num_months

    #The greatest increase in profits (date and amount)
    max_month = time_months[index_max]

    #The greatest decrease in profits (date and amount) over the entire period
    min_profits = min(profit_losses)

#Create output report
output_report = (
    f"Financial Analysis\n"
    f"------------------\n"
    f"Total Months: {num_months}\n"
    f"Total Net: {total_net:.2f}\n"
    f"Average Change: {change_in_loss:.2f}\n"
    f"Greatest Increase in Profits: {greatest_profit_increase[0]} (${greatest_profit_increase[1]:,.2f})\n"
    f"Greatest Decrease in Profits: {greatest_profit_decrease[0]} (${greatest_profit_decrease[1]:,.2f})\n"
)

#print output report
print(output_report)

#export to TXT file
with open(analysis_path, "w") as report_txt:
    report_txt.write(output_report)

