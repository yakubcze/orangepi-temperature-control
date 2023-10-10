#!/usr/bin/env python
# -*- coding: utf-8 -*-

import OPi.GPIO as GPIO
from datetime import datetime

GPIO.setwarnings(False)
GPIO.setboard(GPIO.PCPCPLUS)	# Orange Pi PC board
GPIO.setmode(GPIO.BOARD)	# set up BOARD BCM numbering
GPIO.setup(11, GPIO.OUT)	# set pin 11 as an output

try:
	temp_file = open("/sys/class/thermal/thermal_zone0/temp", "r")
	temp = int(temp_file.read())

	log_file = open("autofanlog.txt", "a")		# LOG
	datetime_obj = datetime.now()			# Datetime object for LOG
	time = datetime_obj.strftime("%H:%M:%S")	# Short time
	date = datetime_obj.strftime("%d.%m %H:%M:%S")	# Long Time

	if temp > 50000:		# If temperature is higher than 50 degrees
		GPIO.output(11, 1)	# Turn fan on
		log_file.write("Turning on fan. Temperature is: {0}. Time is: {1}\n".format(temp, time))
	else:				# Else
		GPIO.output(11, 0)	# Turn fan off
		log_file.write("Turning off fan. Temperature is {0}. Time is: {1}\n".format(temp, time))
except:
	GPIO.cleanup()		# Clean GPIO
	log_file.write("Exception occured! Time is: {0}\n".format(date))
finally:
	temp_file.close()
	log_file.write("Script finished! Time is {0}\n".format(date))
	log_file.close()
