#Import mods
import os
import csv
list
#Path to file 
PyBank_Path = os.path.join('budget_data.csv')
#output
analysis_path = os.path.join('Analysis.txt')

#Variables to store data 
time_months = []
profit_losses = []
total_net= 0
change_in_loss = []
greatest_profit_increase = ["", 0 ]
greatest_profit_decrease = ["", 9999999 ]
max_month = ""
index_min = 0
index_max = 0


#Open CSV
with open(PyBank_Path, "r")as csvfile:
    budget_csv = csv.reader(csvfile, delimiter= ',')


    #Header
    header = next(budget_csv)  

    #Loop
    for i, row in enumerate(budget_csv):
        #Date
        time_months.append(row[0])
        
        #Profit/Loss
        profit_loss = float(row[1])
        profit_losses.append(profit_loss)
        total_net += profit_loss
        
        # Update greatest increase and decrease
        if profit_loss > greatest_profit_increase[1]:
            greatest_profit_increase = [row[0], profit_loss]
            index_max = i
        if profit_loss < greatest_profit_decrease[1]:
            greatest_profit_decrease = [row[0], profit_loss]
            index_min = i

        # Calculate average change in profit/losses
        for i in range(1, len(profit_losses)):
        change_in_loss.append(profit_losses[i] - profit_losses[i-1])
        avg_change_in_loss = sum(change_in_loss) / len(chan

    
#create output report
output_report = (
    f"Financial Analysis\n"
    f"------------------\n"
    f"Total Months: {time_months}\n"
    f"Total Net: {total_net}\n"
    f"Average Change: {avg_change_in_loss:.2f}\n"
    f"Greatest Increase in Prof
)

#print output report
print(output_report)

#export to TXT file
with open(analysis_path, "w") as report_txt:
    report_txt.write(output_report)






 









