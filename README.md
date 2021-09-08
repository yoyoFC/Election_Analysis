# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has give you the following tasks to complete the election audit of a recent local congressional election.The data source was provided in csv format. Here is the list of goals to accomplish this task: 

1. Calculate the total number of votes cast. 
2. Get a complete list of candidates who received votes. 
3. Calculate the total number of votes each candidate received. 
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the elections based on popular vote. 

## Resource
- Data Source: election_results.csv
- Software: Python 3.9.7. Visual Studio Code, 1.60.1

## Election-Audit Results
The analysis of the election shows that:
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Candidate Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
    - Candidate Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.

## Election-Audit Summary
This code was designed with the purpose to be re-usable for other elections. Each section is well documented and the variables names were selected properly to avoid confusion and provide enough information for other developers. This logic can be considered as a template by applying few modifications :

- Source file location: In this version, the file path address for the data source was hard coded. If the election commisssion is looking for a dynamic solution to avoid maniapulate the code, we can take advantage of the "input" function and request the file path address as a mandatory entry for the end user before execute all the calculation:

- Output result layout: The content for the results can be customized based on the election type. Same as the "data source", the file's location for the final result can be manually insert during the program execution. 

- Additional details - Demographic profile: If the data source provides additional information for demographics results such as Sex or Academic level, this code is capable to include results related to those parameters. If the raw data includes a column with these categories : Postgrad, College grad, Some College and Highs school or less; a set of instructions can be inserted inside of the main for loop sequence (see image for more details - Line 79 to 88)
    
