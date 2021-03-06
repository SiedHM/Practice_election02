# Add our dependencies.
import csv
from email import header
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0
# Candidate Options
candidate_options = []
candidate_votes = {}
#opening and reading the data
election_data=open(file_to_load,"r")
file_reader = csv.reader(election_data)
#read the header row
headers = next(file_reader)
print(headers)
for row in file_reader:
    total_votes += 1
    candidate_name = row[2]
    # If the candidate does not match any existing candidate...
    if candidate_name not in candidate_options:
       candidate_options.append(candidate_name)
       candidate_votes[candidate_name] = 0
    candidate_votes[candidate_name] += 1
    
print(total_votes)
print(candidate_votes)
winning_candidate = ""
winning_count = 0
winning_percentage = 0
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = round(float(votes) / float(total_votes) * 100,2)
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name
   

print(winning_candidate)
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)





election_data.close()

