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

#!/usr/bin/python3
# This is a simple robot application written by Dakota James Owen Keeler
# Need for the Raspberry pi (In furture abstract away from main program)
import RPi.GPIO as gpio
# Built in modules
import sys
# Custom
import auton
import net
import telo
import utils

def autonOp():
	auton.readCode()

def teloOp():
	telo.mainTelo()

def main():
	myRobotInit()
	# mode refers to weather its in telo or auton
	# 1 = telo
	# 2 = auton
	# 3 = write mode
	mode = 1	

	if mode == 5:
		try:		
			teloOp()
		except:
			net.writeNc('[ERROR] Could not start teloOp:')
			sys.exit()
	elif mode == 2:
		try:		
			autonOp()
		except:
			net.writeNc('[ERROR] Could not start autonOp:')
			sys.exit()
	else:
		try:		
			#auton.writeCode()
			net.readDs()
		except:
			net.writeNc('[ERROR] Could not start writeCode:')
			sys.exit()
		
main()



