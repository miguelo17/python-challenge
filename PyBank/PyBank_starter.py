# -*- coding: UTF-8 -*-
#"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("/Users/miguela.olmos/Documents/Python Challenge/PyBank/Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("/Users/miguela.olmos/Documents/Python Challenge/PyBank/analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
sum_of_rows = 0
first_row = 0
list = []
suma = 0
newlist = []
average_change = 0
decrease = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data, delimiter=',')

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list

    for row in reader:
        total_months = total_months + 1
        #print (total_months) test to count every row in the file
        
        #print (row[1])   

        list.append(int(row[1]))
        total_net = sum(list)
   # print (total_net)
    
    # Print results of total months and total net change
    print ("Total Months: " + str(total_months))    
    print ("Total Net is: $" + str(total_net))  
    

      # Track the total and net change
    
    average_change = total_net / total_months
    print ("Total Average: $" + str(average_change)) 

    
     # Print results of total months and total net change
    #______________________________________________________
  

    for i in range(len(list)-1):
        decrease = list[i] - list[i+1]
        newlist.append((decrease))
    
    #print (newlist)

    total_decrease = sum(newlist)
    total_decrease = total_decrease / (len (list)-1)
    print("Average Change: $"+ str(total_decrease))

#print (newlist)

max_value = max (newlist)

min_value = min (newlist)

print("Greatest increase in Profits: "+ str(max_value))
print ("Greatest decrease in Profits: " + str(min_value))


       
        # Calculate the greatest increase in profits (month and amount)


        # Calculate the greatest decrease in losses (month and amount)


# Calculate the average net change across the months

    

# Generate the output summary


# Print the output



# Write the results to a text file
with open (file_to_output,"w") as file:
     
     file.write ("Total Months: " + str(total_months)+ str("\n") ) 
     file.write ("Total Net is: $" + str(total_net)+ str("\n")) 
     file.write("Average Change: $"+ str(total_decrease) + str("\n")) 
     file.write("Greatest increase in Profits: "+ str(max_value)+ str("\n"))
     file.write ("Greatest decrease in Profits: " + str(min_value) + str("\n"))

file.close()

