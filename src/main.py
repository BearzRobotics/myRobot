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
from net import *
import utils
import robotControl as roboC
import pygame
from pygame.locals import * 
	
def teloOp():
	net.writeStatus('1')
	
	print('W) Forword')
	print('S) Backwords')
	print('A) Left')
	print('D) Right')
	print('Q) Quit')
	
	while True:
		data = input('->')
		if data == 'S' or data == 's':
			roboC.dBackwords(75)
			time.sleep(1)
			roboC.dBackwords(0)
		if data == 'W' or data == 'w':
			roboC.dForword(75)
			time.sleep(1)		
			roboC.dForword(0)	
		if data == 'A' or data == 'a':
			roboC.dLeft(75)
			time.sleep(1)	
			roboC.dLeft(0)			
		if data == 'D' or data == 'd':
			roboC.dRight(75)
			time.sleep(1)		
			roboC.dRight(0)	
		if data == 'Q' or data == 'q':
			break

	utils.myCleanUp()

def main():
	net.setup()
	# mode refers to weather its in telo or auton
	# 1 = telo
	# 2 = auton
	# 3 = write mode

	#Packet = decrypt.decryptPacket(0)
	#ControlByte = Packet
	#print(ControlByte)
	print("T) = telo")
	print("A) = auton")
	print("W) = write mode")
	mode = input('->')

	if mode == 'T' or mode == 't':
		try:
			teloOp()
		except:
			utils.myCleanUp('[ERROR] Could not start teloOp:')
	elif mode == 'A' or mode == 'a':
		try:
			autton.hardCoded()
			#auton.readCode(1508990571.2707024)
		except:
			utils.myCleanUp('[ERROR] Could not start autonOp:')
	elif mode == 'W' or mode == 'w':
		try:
			auton.writeCode()
		except:
			utils.myCleanUp('[ERROR] Could not start writeCode:')

	else:
			utils.myCleanUp('What did you want me to do, you did not pass in a valid option ')

main()
