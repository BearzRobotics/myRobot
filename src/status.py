#!/usr/bin/python3

#KNOW ALL MEN BY THESE PRESENTS: 'i': man [Dakota James Owen Keeler]
#Copyright this software in the year of our lord 2017 under the GNU
#Public License version 3.
#Contact: bearzrobotics@gmail.com

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

import RPi.GPIO as gpio
import time
import sys
import socket

RdPin =	37
GnPin = 35
BlPin = 33

gpio.setmode(gpio.BOARD) # uses pin numbers 1 -40
gpio.setwarnings(False)
gpio.setup(RdPin, gpio.OUT)
gpio.setup(GnPin, gpio.OUT)
gpio.setup(BlPin, gpio.OUT)

server='127.0.0.1'
def readSp():		# Read status Packet
	Rs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	Port = 7000
	#R.connect((Server, Port))
	Rs.bind(('', Port))	
	Rs.settimeout(100000)
	while True:
		gpio.setmode(gpio.BOARD) # uses pin numbers 1 -40
		data, addr = Rs.recvfrom(4096)
		data = data.decode('utf-8')		
		# 1 = good
		# 2 = Warning
		# 3 = Crital Error
		
		if data == '1':
			gpio.output(RdPin, gpio.LOW)	
			gpio.output(GnPin, gpio.HIGH)
			gpio.output(BlPin, gpio.LOW)
		elif data == '2':
			gpio.output(BlPin, gpio.HIGH)
			gpio.output(RdPin, gpio.LOW)	
			gpio.output(GnPin, gpio.LOW)
		elif data == '3':
			gpio.output(RdPin, gpio.HIGH)	
			gpio.output(BlPin, gpio.LOW)
			gpio.output(GnPin, gpio.LOW)
		elif data == 'kill':
			break
		else:
			print(data) # just to make sure its working

	gpio.cleanup()
	Rs.close()

		
def cCleanUp():
		gpio.output(RdPin, gpio.LOW)	
		gpio.output(GnPin, gpio.LOW)
		gpio.output(BlPin, gpio.LOW)
		gpio.cleanup()


readSp()
