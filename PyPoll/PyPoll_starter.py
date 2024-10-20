# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("/Users/miguela.olmos/Documents/Python Challenge/PyPoll/Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("/Users/miguela.olmos/Documents/Python Challenge/PyPoll/analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates = []
cand1 = 0
cand2 = 0
cand3 = 0
cand1_percent =0
cand2_percent =0
cand3_percent =0
cand_win = []

# Winning Candidate and Winning Count Tracker
winning_candidate = 0
winning_tracker = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(" . ", end="")

        # Increment the total vote count for each row
        total_votes = total_votes + 1
    
        candidates = row [2]
        if candidates == "Charles Casper Stockham":
            cand1 = cand1 +1
        elif candidates =="Diana DeGette":
            cand2 =cand2 +1
        elif candidates =="Raymon Anthony Doane":
            cand3=cand3 +1

print ("Election Results" +str("\n"))
print ("Total Votes: "+ str(total_votes)+str("\n"))

cand1_percent = (cand1 / total_votes)*100
cand1_percent = round(cand1_percent,3)
#print(cand1_percent)
cand2_percent = (cand2 / total_votes)*100
cand2_percent = round(cand2_percent,3)
#print(cand2_percent)
cand3_percent = (cand3 / total_votes)*100
cand3_percent = round(cand3_percent,3)
#print(cand3_percent)


print ("Charles Casper Stockham total votes: " + str(cand1),str(cand1_percent)+str("%") +str("\n"))
print ("Diana Degette total votes: "+str(cand2), str(cand2_percent)+str("%")+str("\n"))
print ("Raymon Anthony Doane total votes: "+str(cand3),str(cand3_percent)+str("%")+str("\n"))

cand_win = {"Charles Casper Stockham" :cand1_percent,"Diana Degette":cand2_percent,"Raymon Anthony Doane":cand3_percent}

#print(cand_win)
maxcand_win = max(cand_win.values())
maxcand_key = max(cand_win, key=cand_win.get)
#print((maxcand_key,maxcand_win))
print("Winner Candidate: " + str(maxcand_key) +str(" ")+ str(maxcand_win)+str("%"))



# Open a text file to save the output
with open(file_to_output, "w") as file:

    # Print the total vote count (to terminal)
    file.write ("Election Results" +str("\n"))
    file.write ("Total Votes: "+ str(total_votes)+str("\n"))

    # Write the total vote count to the text file

    file.write("Charles Casper Stockham total votes: " + str(cand1)+ str(" , "))
    file.write (str(cand1_percent)+str("%") +str("\n"))
    file.write("Diana Degette total votes: "+str(cand2)+str (" , "))
    file.write( str(cand2_percent)+str("%")+str("\n"))
    file.write("Raymon Anthony Doane total votes: "+str(cand3)+str(" , "))
    file.write(str(cand3_percent)+str("%")+str("\n"))
    file.write("Winner Candidate: " + str(maxcand_key) +str(" ")+ str(maxcand_win)+str("%"))

    # Generate and print the winning candidate summary


    # Save the winning candidate summary to the text file

    file.close ()