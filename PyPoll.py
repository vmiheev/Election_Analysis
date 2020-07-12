# The data we need to retrieve. 
# 1. The total number of votes cast
# 2. A complete list of candidated who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Assign a variable for the file to load and the path.
# file_to_load = 'Election_Analysis\Resources\election_results.csv'

# #Open the election results to read the file
# with open(file_to_load) as election_data:

#     #To do: perform analysis
#     print(election_data)
#     print("Hello world")

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Election_Analysis\Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Election_Analysis\Analysis", "election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        total_votes = total_votes + 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float (total_votes) * 100
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})")
    if votes > winning_count and vote_percentage > winning_percentage:
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
#print(candidate_votes)
#print(total_votes)

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("Election_Analysis\Analysis", "election_analysis.txt")
# # Using the open() function with the "w" mode we will write data to the file.
# with open(file_to_save, "w") as txt_file:
#      txt_file.write("Arapahoe\nDenver\nJefferson")