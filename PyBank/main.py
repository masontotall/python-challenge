print("Hello from PyBank")
# make files accessible across platforms
import os

#Read CSV mod
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#improved reading

with open(csvpath) as csvfile:

    csvreader=csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        print(row)




