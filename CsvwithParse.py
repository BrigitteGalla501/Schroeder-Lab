import csv
import time
import pyvisa
import datetime 

y_value = 0 #this will be voltage 
x_value = 0 #this will be Runtime

#added for parsing data
y2_value = 0

fieldnames = ["Run Time", "Voltage", "Voltage Parsed"]

startTime = time.time() # Create a variable that holds the starting timestamp.

#Interfacing with the Keithley!
electrometer = pyvisa.ResourceManager().open_resource('GPIB0::1::INSTR')# Connect to the keithley and set it to a variable named electometer.
##check that the this is the right channel/ that a channel locaion is needed
electrometer.write(":ROUTe:CLOSe (@101)") # Set the keithley to measure channel 1 of card 1
electrometer.write(":SENSe:FUNCtion 'VOLTage'") # Set the keithley to measure voltage.

    
#gets the date and time 
from datetime import datetime   # noqa: E402, F811
now = datetime.now() #makes an object with the date and time 
dt_string = now.strftime("%d/%m/%Y %H:%M:%S") #creates a string of the dates and time.
#print ("date and time =", dt_string)

with open('New2data.csv', 'w') as csv_file:
    csv_writer= csv.DictWriter(csv_file, 'Date and Time:', dt_string) # adds date and time string.
   # csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    with open('New2data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "Run Time": x_value,
            "Voltage": y_value,
            "Voltage Parsed" : y2_value
            
        }
         
        
        csv_writer.writerow(info)
        print(x_value, y_value, y2_value)


        voltageReading = electrometer.query(':SENSe:DATA:FRESh?').split(',')[0][:-2] # Read and process data from the keithley.
        y_value = voltageReading
        x_value = time.time() - startTime

        #getting rid of the E00 in the voltage output
        dataparse= voltageReading.replace("E+00NV", "")
        y2_value = dataparse


    time.sleep(1)