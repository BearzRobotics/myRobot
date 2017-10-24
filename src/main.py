#!/usr/bin/python3
# This is a simple robot application written by Dakota James Owen Keeler
# Need for the Raspberry pi (In furture abstract away from main program)
import RPi.GPIO as gpio
# Built in modules
import math
import logging
import sys
# Custom
import auton
import net
import telo
import utils

def myRobotInit():
	logging.basicConfig(level=logging.DEBUG)

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



