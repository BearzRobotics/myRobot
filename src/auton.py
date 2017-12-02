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


import linecache
import time
import js
import robotControl as roboC

def hardCoded():
	
	startTime = time.time()
	
	while startTime <= 15:
		
		roboC.dBackwords(75)
		time.sleep(1)
		
		roboC.dForword(75)
		time.sleep(1)			
		
		roboC.dLeft(75)
		time.sleep(1)	
					
		
		roboC.dRight(75)
		time.sleep(1)
		
	# Once time is past fiften seconds			
	roboC.killBot()	
		
	

def writeCode():
	TimeVar = time.time()
	FileName = "./adb"
	
	Adb = open(FileName, 'a')
	
	line = "[" + str(TimeVar) + "\n"
	Adb.write(line)
	
	while TimeVar + 15 > time.time():
		# This will evenuly have joystick values passed from qdriverstation
		line = str(js.getAxis('x')) + "," + str(js.getAxis('y')) + "," + str(js.getAxis('z')) + "\n" 
		Adb.write(line)
	while TimeVar + 20 > time.time():
		break
	
	Adb.write("]\n")
	Adb.close()

def readCode(recTime):
	TimeVar = time.time()
	FileName = "./adb"
	
	StartLine = 0
	EndLine = 0
	Count = 0
	
	RecTimeString = "[" + str(recTime)
	
	with open(FileName) as file:
		for line in file:
			Count += 1
			if RecTimeString in line:
				StartLine = Count
			if StartLine !=0 and EndLine == 0 and "]" in line:
				EndLine = Count
				break
	Count = 0
	
	while TimeVar + 15 > time.time() and Count + StartLine < EndLine -1:
		Count += 1
		Line = linecache.getline(FileName, Count + StartLine)
		LineList = Line.split(',')
		
		print(float(LineList[0]), float(LineList[1]), float(LineList[2]))
	
	while TimeVar + 15  > time.time():
		print(0,0,0)
		
	linecache.clearcache()
	
	
	
#readCode(1508990571.2707024)
