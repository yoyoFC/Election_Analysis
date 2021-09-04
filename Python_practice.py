# Creating an empty list
from typing import KeysView


counties = ["Arapahoe","Denver","Jefferson"]

#########################################################################
#If / and / or conditions
#if counties[1] == "Denver":
#    print("yeap it is")
#counties = ["Arapahoe","Denver","Jefferson"]

#if "El Paso" in counties:
#    print("El Paso is in the list of counties.")
#else:
#    print("El Paso is not the list of counties.")

#if "Arapahoe" in counties or "El Paso" in counties:
#    print("Arapahoe and El Paso are in the list of counties.")
#else:
#    print("Arapahoe or El Paso is not in the list of counties.")

#########################################################################
#Iterate through Dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#Method 1 to obtain keys and values :
#for counties in counties_dict.keys():
#    print(f"printing counties using keys:{counties}")

#for votes in counties_dict.values():
#    print(f"Number of votes in order:{votes}")

#Method 2,3 to obtain values:
#for counties in counties_dict:
#    print(f"method 2: {counties_dict[counties]}")
#    print(f"method 3: {counties_dict.get(counties)}")

#Method 4 for printing all items
#for county,Num_votes in counties_dict.items():
#    print(f"{county} county has {Num_votes} registered voters.")

#################################################################
# Iterate through Dictionary inside of List
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

#Nested for loops to get the values - > using the values method
#for county_dict in voting_data:
#    for value in county_dict.values():
#        print(f"nested for loop :{value}")

for i in range(len(voting_data)):
    print(f"{voting_data[i]['county']} county has {voting_data[i]['registered_voters']:,} registered voters.")   

#Example with inputs and formatting result on print
#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))
#message_to_candidate = (
#    f"You received {candidate_votes:,} number of votes. "
#    f"The total number of votes in the election was {total_votes:,}. "
#    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
#print(message_to_candidate)

#Playing with Dependencies/Packages
# Import the datetime class from the datetime module.
import datetime as ts
import random
# Use the now() attribute on the datetime class to get the present time.
now = ts.datetime.now()
# Print the present time.
print("The time right now is ", now)

#Displaye the methods availble using the function dir
print(dir(int))
print(dir(float))
print(dir(random))
#print(dir(numpy))