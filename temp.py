import os
import time
import glob
import sys
from datetime import datetime
from ds18b20 import DS18B20
from json import dumps, load

# Program to read the temperature from a digital sensor attached to the Pi
# Temperature can either read continuosly and printed to standard output,
# or it can be logged to a JSON file.

# Shell commands to the OS to load drivers for sensor
# Ensure that we are in root
os.system('cd /')
# Initiate the sensor
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

# Find the file to which temperature is written
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0] 
device_file = device_folder + '/w1_slave'

# Get the raw data from the file
def read_temp_raw():
	f = open(device_file, 'r')
	lines = f.readlines()
	f.close()
	return lines
	
# Pretty print our data
def read_temp():
	lines = read_temp_raw()
	while lines[0].strip()[-3:] != 'YES':
		time.sleep(0.2)
		lines = read_temp_raw()
	equals_pos = lines[1].find('t=')
	if equals_pos != -1:
		temp_string = lines[1][equals_pos+2:]
		temp_c = float(temp_string) / 1000.0
		return temp_c

# How should we run the program ?

# Continuous write to output
if(sys.argv[1] == 1 ):
	while True:
		print(read_temp())
		time.sleep(1)
# Write to JSON
else:
	# How many hours we will monitor
	monitor_hours = 48
	# How long have we been monitoring
	monitored_hours = 0
	# Make our file
	log_file = open('loggedFile.txt', w+)
	count=0
	
	#Start logging
	while monitored_hours < monitor_hours:
		# Current time and temp
		time_now = datetime.now().minute
		temperature_in_celsius = sensor.get_temperature()
	
		json.dumps({time_now : temperature_in_celsius,}, indent=4, separators=(',', ': '))
		
		count += 1
		# Sleep for 30min
		sleep(1800)
		if(count%2 == 0):
			monitored_hours += 1
		
	log_file.flush()
