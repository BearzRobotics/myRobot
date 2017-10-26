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


# Right now we need to fake out the joystick
import net
import random

def getAxis(axis):
	if axis == 'x':
		return random.randint(1, 4)
		net.writeNc("axis X")
	elif axis == 'y':
		return random.randint(1, 4)
		net.writeNc("axis y")
	elif axis == 'z':
		return random.randint(1, 4)
		net.writeNc("axis z")
	else:
		print("error")
