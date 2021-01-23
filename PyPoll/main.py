print("Hello from PyPoll")
# make files accessible across platforms
import os

#Read CSV mod
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

#improved reading

with open(csvpath) as csvfile:

    csvreader=csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    print(f'CSV Header: {csv_header}')

    for row in csvreader:
        print(row)

    
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)

    total_votes=sum(1 for row in csvreader)
    print(total_votes)
