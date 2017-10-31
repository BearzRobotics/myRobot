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
motorAll = LinkedMotors(m1,m2,m3,m4)
#Names for Individual Arrows
ab = Arrow(1)
al = Arrow(2)
af = Arrow(3) 
ar = Arrow(4)
	
def dBackwords(speed):
	af.off()
	ab.on()
	motorALL.reverse(speed)
	time.sleep(5)
	
def dForword(speed):
	af.off()
	motorALL.forward(speed)
	time.sleep(5)
    
def dLeft(speed):
	ar.on()
	al.off()
	m1.forward(speed)
	m2.forward(speed)
	m3.stop()
	m4.stop()
	time.sleep(5)

def dRight(speed):
	ar.on()
	al.off()
	m3.forward(speed)
	m4.forward(speed)
	m1.stop()
	m2.stop()
	time.sleep(5)
