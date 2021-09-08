#Roadmap
#The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate received (Won)
#4. The total number of votes each candidate won
#5. The winner of the election based on the total number of votes

import csv
import os
path = "/Users/joelf/Documents/Bootcamp/Data_Analytics/Module_3/Election_Analysis"
file_to_load = os.path.join(path,"Resources", "election_results.csv")
file_to_save = os.path.join(path,"analysis", "election_analysis_offline.txt")

#Initialize variables
total_votes = 0
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Print the header row.
    headers = next(file_reader)
    #print(headers)

    #Total votes
    for row in file_reader:
        #Obtain the total number of votes
        total_votes +=1

        #Print the candidate name for each row
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] +=1

#####################################################################################
# Print the final vote count to the terminal.
# Save the results to our text file.
with open(file_to_save, "w") as txt_file: 
    election_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)  

    # Percentage of votes for each candidate
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print/save the candidate name and percentage of votes.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        # Winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #Reference to confirm condition!
            #print(f"{candidate_name} - compare {votes} vs {winning_count}")
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
    txt_file.write(winning_candidate_summary)
