#!/usr/bin/python

import time, signal, sys, socket
from Adafruit_ADS1x15 import ADS1x15

def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
#print 'Press Ctrl+C to exit'

ADS1015 = 0x00  # 12-bit ADC
ADS1115 = 0x01	# 16-bit ADC

# Initialise the ADC using the default mode (use default I2C address)
# Set this to ADS1015 or ADS1115 depending on the ADC you are using!
adc = ADS1x15(ic=ADS1115)
ip = "192.168.2.101"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, 13000))

# Read channel 0 in single-ended mode, +/-4.096V, 250sps

while 1:
	volts = adc.readADCSingleEnded(0, 4096, 250) / 1000
	message = str("%.6f" % volts)
	s.send(message)
	# To read channel 3 in single-ended mode, +/- 1.024V, 860 sps use:
	# volts = adc.readADCSingleEnded(3, 1024, 860)

	print "%.6f" % (volts)
	time.sleep(1)
