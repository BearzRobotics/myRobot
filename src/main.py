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
import sys
# Custom
import auton
import net
from net import ds
import utils
import time
from PiMotor import Motor

# global variables
m1 = Motor("MOTOR1",1)	
m2  = Motor("MOTOR2",1)	
m3 = Motor("MOTOR3",1)	
m4 = Motor("MOTOR4",1)	

gpio.setmode(gpio.BOARD) # uses pin numbers 1 -40
# setup pins on the pi
gpio.setwarnings(False)

def autonOp():
	auton.writeCode()
	
def dBackwords():
	af.off()
	ab.on()
	motorALL.reverse(100)
	net.writeStatus('1')
	time.sleep(5)
	
def dForword():
	af.off()
	motorALL.forward(100)
	net.writeStatus('2') # debug code
    time.sleep(5)
    
def dLeft():
	ar.on()
    al.off()
    m1.forward(100)
    m2.forward(100)
	m3.stop()
    m4.stop()
	net.writeStatus('3')
    time.sleep(5)

def dRight():
	ar.on()
    al.off()
    m3.forward(100)
    m4.forward(100)
	m1.stop()
    m2.stop()
	net.writeStatus('1')
    time.sleep(5)

def teloOp():
	net.writeStatus('1')
	# Creates gloab varible for the telo op def
	#RunningTelo = True

	while RunningTelo == True:
		print("telo")

		data = ds.readDs()
		print(data)
		
		if data == '1':
			dBackwords()
		if data == '2':
			dForword()
		if data == '3':
			dLeft()	
		if data == '4':
			dRight()
		if data == '5':
			RunningTelo = False
				
	myCleanUp()

def myCleanUp(cleanMeassage):
	net.writeNc(cleanMeassage)
	net.writeStatus('3')
	gpio.cleanup()
	sys.exit()

def main():
	# mode refers to weather its in telo or auton
	# 1 = telo
	# 2 = auton
	# 3 = write mode
	
	mode1 = ds.readDs()
	mode = str(mode1)
	
	if mode == '1':
		try:
			teloOp()
		except:
			myCleanUp('[ERROR] Could not start teloOp:')
	elif mode == '2':
		try:
			myRobot.autonOp()
		except:
			myCleanUp('[ERROR] Could not start autonOp:')
	elif mode == '3':
		try:
			net.readDs()
		except:
			myCleanUp('[ERROR] Could not start writeCode:')

	else:
		myCleanUp('What did you want me to do, you did not pass in a valid option ')

main()
