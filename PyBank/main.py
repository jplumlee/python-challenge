#Import os and csv modules so that we can find and import the csv
import os
import csv

#Create os path for csv to be read and the text file to written.
csvpath = os.path.join('Resources', 'budget_data.csv')
text_file = os.path.join('Analysis', 'budget_results.txt')

#Setup variables and list
monthly_average_change_list = []
months = 0
revenue_total = 0
previous_month_revenue = 0
monthly_average_change = 0
total_monthly_change = 0
gincrease = 0
gdecrease = 0

#Open CSV file
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header in the first and skip
    csv_header = next(csvreader)
    
    for row in csvreader:
        #Count number of months/rows in the dataset
        months = months + 1
   
        #Calculate revenue_total by adding each row in the column.
        revenue_total = revenue_total + int(row[1])

        #To get an accurate calc for the monthly average we need to skip the first row after the header or it will take that value
        #The if statement below checks to see if it is the first row and if it is it moves to the next row
        if months == 1:
            previous_month_revenue = int(row[1]) 
            continue
        
        #Calculate average change month to month
        monthly_average_change = int(row[1]) - previous_month_revenue
        previous_month_revenue = int(row[1])

        #Calc total_monthly_change using the results from calculating monthly_average_change
        total_monthly_change = total_monthly_change + monthly_average_change

        #Place the results of calculating montly_average_change into a list
        monthly_average_change_list.append(monthly_average_change)
        #Find the total_average_change by dividing total_monthly_change by length of the monthly_average_change_list
        total_average_change = (total_monthly_change / len(monthly_average_change_list))

        #Calc the greatest increase by looping through each row to find the max
        if monthly_average_change > gincrease:
            gincrease = monthly_average_change
            gincrease_month = row[0]
    
        #Calc the greatest decrease by looping through each row to find the min
        if monthly_average_change < gdecrease:
            gdecrease = monthly_average_change
            gdecrease_month = row[0]
    
    #Print the results to the terminal
    print("Financial Analysis")
    print("--------------------------")
    print(f"Number of Months: {months}")
    print(f"Total: ${revenue_total}")
    print(f"Average Change: ${round(total_average_change, 2)}")
    print(f"Greatest Increase in Profits: {gincrease_month} (${gincrease})")
    print(f"Greatest Decrease in Profits: {gdecrease_month} (${gdecrease})")

    #Write the results to budget_results.txt in the specifed file path.
    with open(text_file, "w") as file:
        # \n creates a break so that the results are displayed correctly in the text file
        file.write("Financial Analysis \n")
        file.write("-------------------------- \n")
        file.write(f"Number of Months: {months} \n")
        file.write(f"Total: ${revenue_total} \n")
        file.write(f"Average Change: ${round(total_average_change, 2)}\n")
        file.write(f"Greatest Increase in Profits: {gincrease_month} (${gincrease})\n")
        file.write(f"Greatest Decrease in Profits: {gdecrease_month} (${gdecrease})\n")