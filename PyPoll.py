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

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    print(headers)
    #for row in file_reader:
    #    print(row)

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

