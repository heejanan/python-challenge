import os
import csv

#Variables
months = []
profitloss_changes = []

total_months = 0 
total_profitloss = 0
prev_month_profitloss = 0
curr_month_profitloss = 0
profitloss_change = 0 

with open ("Resources/budget_data.csv","r") as budgetdata:
    pybank = csv.reader(budgetdata) 

    header = next(budgetdata)

    for row in pybank:
        total_months += 1 

        curr_month_profitloss=int(row[1])
        total_profitloss += curr_month_profitloss

        if (total_months == 1): 
            prev_month_profitloss = curr_month_profitloss

        else:
            profitloss_change = curr_month_profitloss - prev_month_profitloss
            months.append(row[0])
            profitloss_changes.append(profitloss_change)
            prev_month_profitloss=curr_month_profitloss

#The net total amount of "Profit/Losses" over the entire period
    net_profitloss = sum(profitloss_changes)
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
    avrg_profitloss = round(net_profitloss/(total_months-1), 2)
#The greatest increase in profits (date and amount) over the entire period
    greatest_increase = max(profitloss_changes)
    greatest_month_index = profitloss_changes.index(greatest_increase)
    greatest_month = months[greatest_month_index]
#The greatest decrease in profits (date and amount) over the entire period
    worst_decrease = min(profitloss_changes)
    worst_month_index = profitloss_changes.index(worst_decrease)
    worst_month = months[worst_month_index]

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.
print("Financial analysis")
print("--------------------------------------")
print(f"Total months: {total_months}")
print(f"Total: ${total_profitloss}")
print(f"Average change: ${avrg_profitloss}")
print(f"Greatest increase in profits: {greatest_month} (${greatest_increase})")
print(f"Greatest decrease in profits: {worst_month} (${worst_decrease})")

pybank_text_results = os.path.join("Analysis", "pybankresults.txt")
with open(pybank_text_results, "w") as outfile:
    outfile.write("Financial analysis\n")
    outfile.write("--------------------------------------\n")
    outfile.write(f"Total months: {total_months}\n")
    outfile.write(f"Total: ${total_profitloss}\n")
    outfile.write(f"Average change: ${avrg_profitloss}\n")
    outfile.write(f"Greatest increase in profits: {greatest_month} (${greatest_increase})\n")
    outfile.write(f"Greatest decrease in profits: {worst_month} (${worst_decrease})\n")