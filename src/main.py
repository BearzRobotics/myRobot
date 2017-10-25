#!/usr/bin/python3

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

# This is a simple robot application written by Dakota James Owen Keeler
# Need for the Raspberry pi (In furture abstract away from main program)
import RPi.GPIO as gpio
import sys
# Custom
import auton
#import net
import utils

class myRobot:
    # global variables
	Lt_rm =	7	# Left rear motor
	Rt_rm =	40	# Right Rear motor
	Lt_fm =	11	# Left front motor
	Rt_fm =	38	# Right Front motor

	gpio.setmode(gpio.BOARD) # uses pin numbers 1 -40
	# setup pins on the pi
	gpio.setup(Lt_rm, gpio.OUT)
	gpio.setup(Rt_rm, gpio.OUT)
	gpio.setup(Lt_fm, gpio.OUT)
	gpio.setup(Rt_fm, gpio.OUT)

	def autonOp():
		auton.readCode()

	def teloOp():
		# Creates gloab varible for the telo op def
		RunningTelo = True
		timer = 0

		while RunningTelo == True:
			print("telo")
			ChanList = (Lt_rm, Rt_rm, Lt_fm, Rt_fm)
			gpio.output(ChanList, HIGH)

		gpio.cleanup()
		sys.exit()

	def main():
		# mode refers to weather its in telo or auton
		# 1 = telo
		# 2 = auton
		# 3 = write mode
		mode = '1'	

		if mode == '1':
			try:		
				myRobot.teloOp()
			except:
				#net.writeNc('[ERROR] Could not start teloOp:')
				sys.exit()
				
		elif mode == '2':
			try:		
				myRobot.autonOp()
			except:
				#net.writeNc('[ERROR] Could not start autonOp:')
				sys.exit()
		else:
			try:		
				#auton.writeCode()
				#net.readDs()
				pass
			except:
				#net.writeNc('[ERROR] Could not start writeCode:')
				sys.exit()
				
if __name__ == '__main__':
	myRobot.main()



