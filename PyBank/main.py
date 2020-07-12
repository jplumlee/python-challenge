import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
text_file = os.path.join('Analysis', 'budget_results.txt')

monthlyaveragechangelist = []

months = 0
revenuetotal = 0
previousmonthrevenue = 0
monthlyaveragechange = 0
totalmonthlychange = 0
gincrease = 0
gdecrease = 0

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    
    for row in csvreader:
        #Count number of months/rows in the dataset
        months = months + 1
        if months == 1:
            previousmonthrevenue = int(row[1]) 
            continue
        #Calculate total profit
        revenuetotal = revenuetotal + int(row[1])
        #Calculate average change month to month
        
        monthlyaveragechange = int(row[1]) - previousmonthrevenue
        previousmonthrevenue = int(row[1])

        totalmonthlychange = totalmonthlychange + monthlyaveragechange

        # Calculate average change in profits/losses
        monthlyaveragechangelist.append(monthlyaveragechange)
        totalaveragechange = (totalmonthlychange / len(monthlyaveragechangelist))

        if monthlyaveragechange > gincrease:
            gincrease = monthlyaveragechange
            gincreasemonth = row[0]
    
        if monthlyaveragechange < gdecrease:
            gdecrease = monthlyaveragechange
            gdecreasemonth = row[0]

    print(f"Number of Months: {months}")
    print(f"Total: ${revenuetotal}")
    print(f"Average Change: ${round(totalaveragechange, 2)}")
    print(f"Greatest Increase in Profits: {gincreasemonth} (${gincrease})")
    print(f"Greatest Decrease in Profits: {gdecreasemonth} (${gdecrease})")

    with open(text_file, "w") as file:
        file.write(f"Number of Months: {months} \n")
        file.write(f"Total: ${revenuetotal} \n")
        file.write(f"Average Change: ${round(totalaveragechange, 2)}\n")
        file.write(f"Greatest Increase in Profits: {gincreasemonth} (${gincrease})\n")
        file.write(f"Greatest Decrease in Profits: {gdecreasemonth} (${gdecrease})\n")