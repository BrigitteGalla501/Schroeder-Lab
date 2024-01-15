#from numpy import void
import pyvisa
import csv

electrometer = pyvisa.ResourceManager().open_resource('GPIB0::1::INSTR') # Connect to the keithley and set it to a variable named electrometer.


electrometer.write(":SENSe:FUNCtion 'VOLTage'") # Set the keithley to measure voltage

print(electrometer.query(':SENSe:DATA:FRESh?')) # Collect the most recently measured data

electrometer.write(":ROUTe:OPEN:ALL") # Open all card channels and thereby set the keithley to measure the front panel inputs.

electrometerData= electrometer.query(':SENSe:DATA:FRESh?')
print(electrometer.query(':SENSe:DATA:FRESh?')) # Collect the most recently measured data

#writing data to a csv
with open('Data.csv', 'w', newline= '') as file:
    writer = csv.writer(file)
    field = ["Voltage"]

    writer.writerow('field')
    writer.writerow({ electrometer.query(':SENSe:DATA:FRESh?')})
    