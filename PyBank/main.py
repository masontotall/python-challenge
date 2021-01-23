print("Hello from PyBank")
# make files accessible across platforms
import os

#Read CSV mod
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#improved reading

with open(csvpath) as csvfile:

    csvreader=csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    print(f'CSV Header: {csv_header}')

    for row in csvreader:
        print(row)

 #count the number of months and print financial analysis   
with open (csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    
    #skip header
    csv_header= next(csvreader)
    
    #count mponths
    total_months = sum(1 for row in csvreader)

    #assign value to variables to 'profit' 'sum of losses' 'sum of profits' and 'total profits'  
    #to be used for profit calculation

with open (csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csv_header=next(csvreader)

    profit_sums=0
    loss_sums=0
    total_profit=0
    profit=0
    


    for row in csvreader:
        profit= int(row[1])
        if profit > 0:
            profit_sums= profit_sums + profit
        elif profit < 0:
            loss_sums = loss_sums + profit
        total_profit= profit_sums + loss_sums
        
    print("Financial Analysis")
    print("---------------------------------")
    print(f'"Total Months: {total_months}"')
    print(f'"Total Profits: {total_profit}"')

    

    

    


        











