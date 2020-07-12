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
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
    # for row in file_reader:
    #     print(row)

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("Election_Analysis\Analysis", "election_analysis.txt")
# # Using the open() function with the "w" mode we will write data to the file.
# with open(file_to_save, "w") as txt_file:
#      txt_file.write("Arapahoe\nDenver\nJefferson")