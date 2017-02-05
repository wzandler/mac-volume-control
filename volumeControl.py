import os
import serial

# Dependencies:
# https://github.com/pyserial/pyserial


# Python listens on a port
ser = serial.Serial('/dev/tty.usbmodem1411', 9600)
volume = ""
while True:
	# read in the value from arduino
	response = ser.readline().decode("utf-8").strip()
	# make sure the value isn't null
	if(response):
		# if the response is different
		if(volume != response):
			print(volume)
			volume = response
			# call apple script to change the volume
			command = 'osascript -e "Set volume ' + volume + '"'
			os.system(command)