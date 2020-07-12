#Import os and csv modules so that we can find and import the csv
import os
import csv

#Create os path for csv to be read and the text file to written.
csvpath = os.path.join('Resources', 'election_data.csv')
text_file = os.path.join('Analysis', 'election_results.txt')

#Setup our list for finding total votes, the dictionary to hold the candidate names and votes they receieved, and set the votecount to 0 for our loop.
total_votes_list = []
candidates_names_dict = {}
vote_count = 0

#Open CSV file
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first and skip
    csv_header = next(csvreader)
    
    # Find the total number of votes cast
    for row in csvreader:
        total_votes_list.append(row[0])
        total_votes = len(total_votes_list)

    #https://realpython.com/iterate-through-dictionary-python/
    #Set candidate variable to column containing names. Create dictionary with candidate as the key and the value to the number occurences of the candidate's name.
        candidate = row[2]
        if candidate in candidates_names_dict:
            candidates_names_dict[candidate] = candidates_names_dict[candidate] + 1
        else:
            candidates_names_dict[candidate] = 1

    # https://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops
    #Iterate over dictionary to find which candidate had the most votes and declare them the winner. 
    for key, val in candidates_names_dict.items():
        if val > vote_count:
            vote_count = val
            winner = key
    
    #Print the results to the terminal
    print("Election Results")
    print("------------------------")
    print(f"Total Votes: {total_votes}")
    print("------------------------")
    #Iterate over dictionary to print candidate (key), calculate the percent of votes, and the value.
    #I could not find a better way to calculate the percent of votes and have it displayed with the correct candidate.
    for key, val in candidates_names_dict.items():
        print(f"{key}: {round(val/total_votes * 100, 2)}% ({val})")
    print("------------------------")
    print(f"Winner: {winner}")
    print("------------------------")

    #Write the results to election_results.txt in the specifed file path.
    with open(text_file, "w") as file:
        # \n creates a break so that the results are displayed correctly in the text file
        file.write("Election Results \n")
        file.write("------------------------\n")
        file.write(f"Total Votes: {total_votes}\n")
        file.write("------------------------\n")
        for key, val in candidates_names_dict.items():
            file.write(f"{key}: {round(val/total_votes * 100, 2)}% ({val}) \n")
        file.write("------------------------\n")
        file.write(f"Winner: {winner}\n")
        file.write("------------------------\n")
        file.close()