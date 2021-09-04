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
file_to_save = os.path.join(path,"analysis", "election_analysis.txt")

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
    #print(candidate_votes)

    # Percentage of votes for each candidate
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

        # Winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #Reference to confirm condition!
            #print(f"{candidate_name} - compare {votes} vs {winning_count}")
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)


#####################################################################################
#Writing methods:
#Method 1 - Using the open the file as a text file.
#outfile = open(file_to_save, "w")
#Write some data to the file.
#outfile.write("Hello World")
#outfile.close()

#Method 2 - using the with statement
with open(file_to_save,"w") as txt_file:
    #Write some data to the file
    #txt_file.write("Hola mundo!")
    #txt_file.write("Arapahoe, ")
    txt_file.write("Counties in the Election\n")
    txt_file.write("-------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
txt_file.close()

