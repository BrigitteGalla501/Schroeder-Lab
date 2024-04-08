import time
import matplotlib.pyplot as plt
import csv
import pyvisa

y_value = 0 #this will be voltage 
x_value = 0 #this will be Runtime

#added for parsing data
y2_value = 0 #this is parsed voltage

fieldnames = ["Time", "Voltage", "Voltage with Units", "Date and Time"]

#These are the lists that the data will be placed in. 
#These can fill up but shouldn’t do so unless it is run continuously for several months.
TimeList= []
VoltageList= []
VwUnitsList= []
date= []

startTime = time.time() # Create a variable that holds the starting timestamp.

#Connecting with the Keithley equipment 
# Initialize the keithley and create some useful variables
electrometer = pyvisa.ResourceManager().open_resource('GPIB0::1::INSTR')# Connect to the keithley and set it to a variable named electometer.
##check that the this is the right channel/ that a channel locaion is needed
electrometer.write(":ROUTe:CLOSe (@101)") # Set the keithley to measure channel 1 of card 1
electrometer.write(":SENSe:FUNCtion 'VOLTage'") # Set the keithley to measure voltage.


    
#gets the date and time 
from datetime import datetime   # noqa: E402
now = datetime.now() #makes an object with the date and time 
dt_string = now.strftime("%d/%m/%Y %H:%M:%S") #creates a string of the dates and time.
print ("date and time =", dt_string)

# Setup the plot 
plt.figure(figsize=(10,10)) # Initialize a matplotlib figure
plt.xlabel('Elapsed Time (s)', fontsize=12) # Create a label for the x axis and set the font size to 24pt
plt.xticks(fontsize=9) # Set the font size of the x tick numbers to 9pt
plt.ylabel('Voltage (V)', fontsize=12) # Create a label for the y axis and set the font size to 24pt
plt.yticks(fontsize=9) # Set the font size of the y tick numbers to 9pt
titleText= ('Voltage (V) vs Time: ', dt_string) ## makes a string out of the Voltage Vs Time plus the current date and time.
plt.title(titleText) #title for the graph

i=0

#This is to have the user input the name of the csv file into the terminal
#Having the name as a variable removes human error by making sure that the name matches in all the areas.
csvName = input ('Please enter the name the Csv file.\n')
titlefile = csvName + '.csv'

## READ THIS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Create a while loop that continuously measures and plots data from the keithley forever.
with open(titlefile, 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    #gets the date and time 
    from datetime import datetime   # noqa: E402
    now = datetime.now() #makes an object with the date and time 
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S") #creates a string of the dates and time.
    print ("date and time =", dt_string)

    with open(titlefile, 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "Time": x_value,
            "Voltage": y2_value,
            "Voltage with Units": y_value,
            "Date and Time": dt_string
        }
        voltageReading = electrometer.query(':SENSe:DATA:FRESh?').split(',')[0][:-2] # Read and process data from the keithley.
        y_value = voltageReading
        x_value = time.time() - startTime

        #getting rid of the E00 in the voltage output
        dataparse= voltageReading.replace("E+00NV", "")
        y2_value = dataparse

        time.sleep(0.5) # Interval to wait between collecting data points.
        TimeList.append(x_value)
        VoltageList.append(y2_value)
        VwUnitsList.append(y_value)

        plt.plot(TimeList, VoltageList, color='blue', linewidth=1.5) # Plot the collected data with time on the x axis and voltage on the y axis.
        plt.pause(0.01) # This command is required for live plotting. This allows the code to keep running while the plot is shown.
        #plt.autoscale()
        i= i+1 
        csv_writer.writerow(info)
        print(x_value, y2_value, y_value)


    time.sleep(5)
    #should save graph when looped
    print("Saving figure!!!")
    plt.savefig( csvName + '.png', bbox_inches = 'tight', pad_inches = .5) ## Names the file of the graph and saves it. Also it formats the file into a png and makes the image have nice margins.    



       
       
            
        
            

    

    

