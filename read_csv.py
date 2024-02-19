import csv
import time
import pyvisa
import datetime 

y_value = 0 #this will be voltage 
x_value = 0 #this will be Runtime


fieldnames = ["Time", "Voltage"]

startTime = time.time() # Create a variable that holds the starting timestamp.

#Interfacing with the Keithley!
electrometer = pyvisa.ResourceManager().open_resource('GPIB0::1::INSTR')# Connect to the keithley and set it to a variable named electometer.
##check that the this is the right channel/ that a channel locaion is needed
electrometer.write(":ROUTe:CLOSe (@101)") # Set the keithley to measure channel 1 of card 1
electrometer.write(":SENSe:FUNCtion 'VOLTage'") # Set the keithley to measure voltage.

    
#gets the date and time 
#from datetime import datetime  #commented out 1/30/2024 since imported up top may not need here anymore 
now = datetime.now() #makes an object with the date and time 
dt_string = now.strftime("%d/%m/%Y %H:%M:%S") #creates a string of the dates and time.
print ("date and time =", dt_string)

with open('data.csv', 'w') as csv_file:
    csv_file.wtiterow(['Date and Time: ', dt_string]) # adds date and time string.
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "Run time": x_value,
            "Voltage": y_value,
            
            
        }

        csv_writer.writerow(info)
        print(x_value, y_value)


        voltageReading = electrometer.query(':SENSe:DATA:FRESh?').split(',')[0][:-2] # Read and process data from the keithley.
        y_value = voltageReading
        x_value = time.time() - startTime


    time.sleep(1)