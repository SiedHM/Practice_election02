# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers=next(file_reader)
    for row in file_reader:
        total_votes +=1
    
    
 
    # Print each row in the CSV file.
    
    


# 3. Print the total votes.
print(total_votes)