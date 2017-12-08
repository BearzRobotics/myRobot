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

# Pin layout being used
#{'f': 15, 'e': 11, 'r': 13}
#{'f': 16, 'e': 22, 'r': 18}
#{'f': 21, 'e': 19, 'r': 23}
#{'f': 24, 'e': 32, 'r': 26}



import RPi.GPIO as gpio
import sys
import time
from PiMotor import *

gpio.setmode(gpio.BOARD) # uses pin numbers 1 -40
# setup pins on the pi
gpio.setwarnings(False)

# global variables
m1 = Motor("MOTOR1",1)
m2 = Motor("MOTOR2",1)
m3 = Motor("MOTOR3",1)
m4 = Motor("MOTOR4",1)

#To drive all motors together
motorALL = LinkedMotors(m1,m2,m3,m4)
#Names for Individual Arrows
ab = Arrow(1)
al = Arrow(2)
af = Arrow(3)
ar = Arrow(4)

def dBackwards(speed):
	motorALL.reverse(speed)

def dForward(speed):
	motorALL.forward(speed)

def dLeft(speed):
	m3.stop()
	m4.forward(speed)
	m1.forward(speed)
	m2.forward(speed)
	time.sleep(.1)
	
	
def dRight(speed):
	m3.forward(speed)
	m4.stop()
	m1.forward(speed)
	m2.forward(speed)
	time.sleep(.1)
	
	
def killBot():
	dBackwords(0)
	dForword(0)
	dLeft(0)
	dRight(0)
	
	
# this is modled afte r	
def drive(x=0 ,y=0 , z=0):
	if x > 0.05:
		print("x: " , x * 100)
		dLeft(x * 100)	
	elif x < -0.05:
		print("x: " , x * 100)
		dRight((x * -1) * 100)	
	else:
		dRight(0)
		dLeft(0)
	
	if y > 0.08:
		print("y: " , y * 100)
		dBackwards(y * 100)
	elif y < -0.08:
		print("y: " , y * 100)
		dForward((y * -1) * 100)
	else:
		dForward(0)
		dBackwards(0)
	