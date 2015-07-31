import time
import post_data
import temperature3

import os
import RPi.GPIO as GPIO
import requests
import analog
import post_data


# change these as desired - they're the pins connected from the
# SPI port on the ADC to the Cobbler
SPICLK = 18
SPIMISO = 23
SPIMOSI = 24
SPICS = 25


# set up the SPI interface pins
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)
while True:
        channel =0
	value =analog. readadc(channel, SPICLK, SPIMOSI, SPIMISO, SPICS)        
	tempc=temperature3.get_temp()
        tempk=tempc+273
	lan=41.14
        lon=-81.35
        user="xhan5"
	zip="44240"
        print "post data"
        print "temp:",tempk
      	print "value:", value
    # post something to a stream

       	name=post_data.post_data(user,lan,lon,tempc,value,zip,test=False)
    	time.sleep(300)

