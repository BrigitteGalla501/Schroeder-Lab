import pyvisa
import time
import matplotlib.pyplot as plt
#import matplotlib.cbook as cbook
import csv



# Initialize the keithley and create some useful variables
electrometer = pyvisa.ResourceManager().open_resource('GPIB0::1::INSTR')# Connect to the keithley and set it to a variable named electometer.
##check that the this is the right channel/ that a channel locaion is needed
electrometer.write(":ROUTe:CLOSe (@101)") # Set the keithley to measure channel 1 of card 1
electrometer.write(":SENSe:FUNCtion 'VOLTage'") # Set the keithley to measure voltage.
timeList = [] # Create an empty list to store time values in.
voltageList = [] # Create an empty list to store voltage values in.
startTime = time.time() # Create a variable that holds the starting timestamp.

#with open('voltageData.csv', 'w', newline= '') as file:
    #writer = csv.writer(file)
    #field = ["Voltage", "Time"]

    #writer.writerow(field)
    #this line isn't quite right
    #writer.writerow({ voltageList, timeList})
    
# Setup the plot 
plt.figure(figsize=(10,10)) # Initialize a matplotlib figure
plt.xlabel('Elapsed Time (s)', fontsize=24) # Create a label for the x axis and set the font size to 24pt
plt.xticks(fontsize=9) # Set the font size of the x tick numbers to 18pt
plt.ylabel('Voltage ($^\circ$C)', fontsize=24) # Create a label for the y axis and set the font size to 24pt
plt.yticks(fontsize=9) # Set the font size of the y tick numbers to 18pt

i= 0
#row = {'Voltage': 'Y1', 'Time':'Y2'}
# Create a while loop that continuously measures and plots data from the keithley forever.
#while True:
while True:
    voltageReading = electrometer.query(':SENSe:DATA:FRESh?').split(',')[0][:-2] # Read and process data from the keithley.
    voltageList.append(voltageReading) # Append processed data to the voltage list
    timeList.append(float(time.time() - startTime)) # Append time values to the time list
    with open('voltageData.csv', 'w', newline= '') as file:
        writer = csv.writer(file)
       
        field = ["Voltage", "Time"]

        writer.writerow(field)
        #this line isn't quite right
        writer.writerow({ voltageReading, time.time()})
    
        writer.writerow({i , i})


    time.sleep(0.5) # Interval to wait between collecting data points.
    i = i +1
    plt.plot(timeList, voltageList, color='blue', linewidth=1.5) # Plot the collected data with time on the x axis and voltage on the y axis.
    plt.pause(0.01) # This command is required for live plotting. This allows the code to keep running while the plot is shown.
    

   

