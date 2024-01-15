from matplotlib import axes
from matplotlib.axis import YAxis
import numpy as np
import pyvisa
import time
import matplotlib.pyplot as plt
import csv

from Python.Python312.Lib.email.mime.image import _png



# Initialize the keithley and create some useful variables
electrometer = pyvisa.ResourceManager().open_resource('GPIB0::1::INSTR')# Connect to the keithley and set it to a variable named electometer.
##check that the this is the right channel/ that a channel locaion is needed
electrometer.write(":ROUTe:CLOSe (@101)") # Set the keithley to measure channel 1 of card 1
electrometer.write(":SENSe:FUNCtion 'VOLTage'") # Set the keithley to measure voltage.
timeList = [] # Create an empty list to store time values in.
voltageList = [] # Create an empty list to store voltage values in.
startTime = time.time() # Create a variable that holds the starting timestamp.

    
#gets the date and time 
from datetime import datetime 
now = datetime.now() #makes an object with the date and time 
dt_string = now.strftime("%d/%m/%Y %H:%M:%S") #creates a string of the dates and time.
print ("date and time =", dt_string)

# Setup the plot 
plt.figure(figsize=(10,10)) # Initialize a matplotlib figure
plt.xlabel('Elapsed Time (s)', fontsize=12) # Create a label for the x axis and set the font size to 24pt
plt.xticks(fontsize=9) # Set the font size of the x tick numbers to 18pt
plt.ylabel('Voltage (V)', fontsize=12) # Create a label for the y axis and set the font size to 24pt
plt.yticks(fontsize=9) # Set the font size of the y tick numbers to 18pt

titleText= ('Voltage (V) vs Time: ', dt_string) ## makes a string out of the Voltage Vs Time plus the current date and time.
plt.title(titleText) #title for the graph


i= 0

## READ THIS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#This determins how long the sampling is. 
#each loop is about 1 sec, 30 loops = 28 seconds 
sampleLength = 31 #This is how many loops the program will be through before stopping.

# Create a while loop that continuously measures and plots data from the keithley forever.
#while True:
with open('fixYonGraph2.csv', 'w', newline='') as file:
    file = csv.writer(file)
    file.writerow(['Date and time', dt_string]) # This adds a date and time header to the data.
    #add header
    file.writerow(['Voltage', 'Time'])
    for i in range(sampleLength):
        #make array for the voltage and time 
        timeArray = np.array([0])
        voltageArray= np.array([0])

        voltageReading = electrometer.query(':SENSe:DATA:FRESh?').split(',')[0][:-2] # Read and process data from the keithley.
        voltageList.append(voltageReading) # Append processed data to the voltage list
        timeList.append(float(time.time() - startTime)) # Append time values to the time list

        #add in the new readings into the array
        timeArray.append(time.time-startTime)
        voltageArray.append(voltageReading)
        xAndy= np.column_stack([timeArray, voltageArray])


        file.writerow({ voltageReading, time.time()- startTime})
    
        plt.locator_params(axis='y', nbins= 15)
        plt.locator_params(axis='x', nbins= sampleLength)

        time.sleep(0.5) # Interval to wait between collecting data points.
        plt.plot(timeList, voltageList, color='blue', linewidth=1.5) # Plot the collected data with time on the x axis and voltage on the y axis.
        ##plt.yticks(np.arange(len(voltageList)), voltageList)
        plt.pause(0.01) # This command is required for live plotting. This allows the code to keep running while the plot is shown.
        #plt.autoscale()
        i= i + 1
        if i == sampleLength-1:
            print("Saving figure!!!")
            plt.savefig('FixY2.png', bbox_inches = 'tight', pad_inches = .5) ## Names the file of the graph and saves it. Also it formats the file into a png and makes the image have nice margins. 

        
            

    

    

