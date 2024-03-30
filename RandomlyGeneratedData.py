import time
import matplotlib.pyplot as plt
import csv
import random


x_value = 0
total_1 = 1000
total_2 = 1000

fieldnames = ["x_value", "total_1", "total_2", "Date and Time"]

XvalueList= []
total1List= []
total2List= []


#gets the date and time 
from datetime import datetime   # noqa: E402
now = datetime.now() #makes an object with the date and time 
dt_string = now.strftime("%d/%m/%Y %H:%M:%S") #creates a string of the dates and time.
print ("date and time =", dt_string) 


# Setup the plot 
plt.figure(figsize=(8,8)) # Initialize a matplotlib figure #{You can change how big the graph shows up here}
plt.xlabel('Elapsed Time (s)', fontsize=12) # Create a label for the x axis and set the font size to 12pt
plt.xticks(fontsize=9) # Set the font size of the x tick numbers to 9pt
plt.ylabel('Voltage (V)', fontsize=12) # Create a label for the y axis and set the font size to 12pt
plt.yticks(fontsize=9) # Set the font size of the y tick numbers to 9pt
titleText= ('Voltage (V) vs Time: ', dt_string) ## makes a string out of the Voltage Vs Time plus the current date and time.
plt.title(titleText) #title for the graph


i= 0

csvName = input ('Please enter the name the Csv file.\n')
print(csvName)
titlefile = csvName + '.csv'

## READ THIS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Create a while loop that continuously measures and plots data from the keithley forever.
with open(titlefile, 'w') as csv_file:  #(Change the name of the csv file before each new experiment)
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()


while True:
    #gets the date and time 
    from datetime import datetime   # noqa: E402
    now = datetime.now() #makes an object with the date and time 
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S") #creates a string of the dates and time.
    print ("date and time =", dt_string)

    with open(titlefile, 'a') as csv_file: #Make sure the name of the CSV matches the name above 
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        #These are the values that are goind to be used for graphing and go into the csv
        #make sure that the orange ones on the left match the Fieldnames above.
        info = {
            "x_value": x_value,
            "total_1": total_1,
            "total_2": total_2,
            "Date and Time": dt_string
        }
    
        #time.sleep(0.5) # Interval to wait between collecting data points.

        #The lists are what are being graphed. They will eventually fill up. 
        #To try and extend the life of the lists you can increase the amount of time between data gatherings 
        XvalueList.append(x_value)
        total1List.append(total_1)
        total2List.append(total_2)

        

        plt.plot(XvalueList, total1List, color='blue', linewidth=1.5) # Plot the collected data with time on the x axis and voltage on the y axis.
        plt.pause(0.01) # This command is required for live plotting. This allows the code to keep running while the plot is shown.
       
        i= i+1 
        csv_writer.writerow(info)
        print(x_value, total_1, total_2)

        x_value += 1
        total_1 = total_1 + random.randint(-6, 8)
        total_2 = total_2 + random.randint(-5, 6)

    time.sleep(2) #this is in seconds   
   
#should save graph when loop is broken
    print("Saving figure!!!")
    plt.savefig( titlefile + '.png', bbox_inches = 'tight', pad_inches = .5) ## Names the file of the graph and saves it. Also it formats the file into a png and makes the image have nice margins.            
##try moving the datetime code to after row 76 to add the date time next to each data point
##could also try having a loop were every 10 (or more) data point have date and time 
    

       
            
        
            

