# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.The data source was provided in csv format. Here is the list of goals to accomplish with this task:

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

<p align="center"><img src="https://user-images.githubusercontent.com/88695570/132615105-480d4a4b-97d6-43e3-a10b-da2a9f019d5c.png">
    
<p align="center"><img src="https://user-images.githubusercontent.com/88695570/132615261-f85c99e8-53ab-4030-a0c7-703f6602aad0.png">

## Election-Audit Summary
This code was designed to be re-usable for other elections. Each section is well documented and the variables names were selected properly to avoid confusion and provide enough information for other developers. This logic can be considered as a template by applying some modifications:

- Source file location: In this version, the file path address for the data source was hard coded. If the election commission is looking for a dynamic solution to avoid manipulate the code, we can take advantage of the "input" function and request the file path address as a mandatory entry for the end user before execute all the calculations:

<p align="center"><img src="https://user-images.githubusercontent.com/88695570/132616178-e40b49b5-36f9-4a25-9795-72de6f14d6c8.png">
    
- Output result layout: The content for the results can be customized based on the election type. Same as the "data source", the file's location for the final result can be manually inserted during the program execution by calling the "input" method.

- Additional details - Demographic profile: If the data source provides additional information for demographic results, such as Sex or Academic level, this code can be capable of including results related to those parameters. If the raw data includes a column with these categories: Postgrad, College grad, Some College, and Highs school or less, a set of instructions can be inserted inside of the main "for" loop sequence. Here is an example about the location for the addditional code : 
    - Variable declaration
    
    <p align="center"><img src="https://user-images.githubusercontent.com/88695570/132617381-5b442874-8493-4544-b2b6-a9a24afe5dad.png">

    - Get the "Academic info" from the data source (assuming the data is located on the 4th column)

    <p align="center"><img src="https://user-images.githubusercontent.com/88695570/132617396-9ec84a41-ea8e-481c-9d35-7757aa2110a5.png">

    - Command to perform the calculation
        
   <p align="center"><img src="https://user-images.githubusercontent.com/88695570/132617395-434764a0-6612-4312-b9f8-cd5610977816.png">

