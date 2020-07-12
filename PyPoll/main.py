import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

totalvoteslist = []
candidatesNamesdict = {}
totalvotes = 0
votecount = 0

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    
    for row in csvreader:
        # The total number of votes cast
        totalvoteslist.append(row[0])
        totalvotes = len(totalvoteslist)

        candidate = row[2]
        if candidate in candidatesNamesdict:
            candidatesNamesdict[candidate] = candidatesNamesdict[candidate] + 1
        else:
            candidatesNamesdict[candidate] = 1
# https://www.pythonforbeginners.com/dictionary/how-to-use-dictionaries-in-python#:~:text=About%20Dictionaries%20in%20Python,with%20commas%20%2C%20between%20each%20pair.&text=As%20with%20lists%20we%20can,printing%20the%20reference%20to%20it.
    for key, val in candidatesNamesdict.items():
        percentofvotes = round(val/totalvotes * 100, 2)

    for key, val in candidatesNamesdict.items():
        if val > votecount:
            votecount = val
            winner = key

    print("Election Results")
    print("------------------------")
    print(f"Total Votes: {totalvotes}")
    print("------------------------")
    for key, val in candidatesNamesdict.items():
        print(f"{key}: {round(val/totalvotes * 100, 2)}% ({val})")
    print("------------------------")
    print(f"Winner: {winner}")
    print("------------------------")