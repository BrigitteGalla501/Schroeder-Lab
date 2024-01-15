import pyvisa

electrometer = pyvisa.ResourceManager().open_resource('GPIB0::1::INSTR') # Connect to the keithley and set it to a variable named electrometer.

##check to see if this is right
electrometer.write(":ROUTe:CLOSe (@101)") # Set the keithley to measure channel 1 of card 1

electrometer.write(":SENSe:FUNCtion 'VOLTage'") # Set the keithley to measure voltage

print(electrometer.query(':SENSe:DATA:FRESh?')) # Collect the most recently measured data

electrometer.write(":ROUTe:OPEN:ALL") # Open all card channels and thereby set the keithley to measure the front panel inputs.

print(electrometer.query(':SENSe:DATA:FRESh?')) # Collect the most recently measured data