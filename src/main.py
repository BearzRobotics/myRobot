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
import robotControl as roboC

def teloOp():
	net.writeStatus('1')
	# Creates gloab varible for the telo op def
	#RunningTelo = True

	while RunningTelo == True:
		print("telo")

		data = ds.readDs()
		print(data)
		
		if data == '1':
			roboC.dBackwords(100)
		if data == '2':
			roboC.dForword(100)
		if data == '3':
			roboC.dLeft(100)	
		if data == '4':
			roboC.dRight(100)
		if data == '5':
			RunningTelo = False
				
	utils.myCleanUp()

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
			utils.myCleanUp('[ERROR] Could not start teloOp:')
	elif mode == '2':
		try:
			myRobot.autonOp()
		except:
			utils.myCleanUp('[ERROR] Could not start autonOp:')
	elif mode == '3':
		try:
			net.readDs()
		except:
			utils.myCleanUp('[ERROR] Could not start writeCode:')

	else:
		utils.myCleanUp('What did you want me to do, you did not pass in a valid option ')

main()
