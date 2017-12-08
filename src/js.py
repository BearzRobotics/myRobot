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
import pygame, sys

pygame.init()
pygame.joystick.init()
try:
	pygame.joystick.Joystick(0).init()
except:
	print("Please Connect a joystick and restart the program")
	sys.exit()
	
def getAxis(axis):
	pygame.event.pump()
	if axis == 'x':
		return round(pygame.joystick.Joystick(0).get_axis(0), 2)
		net.writeNc("axis X")
	elif axis == 'y':
		return round(pygame.joystick.Joystick(0).get_axis(1), 2)
		net.writeNc("axis y")
	elif axis == 'z':
		return round(pygame.joystick.Joystick(0).get_axis(2), 2)
		net.writeNc("axis z")
	else:
		print("error")
		
def getButton(button):
	if button == "x":
		return pygame.joystick.Joystick(0).get_button(0)
	if button == "o":
		return pygame.joystick.Joystick(0).get_button(1)
	if button == "tri":
		return pygame.joystick.Joystick(0).get_button(2)
	if button == "sq":
		return pygame.joystick.Joystick(0).get_button(3)	
	
	if button == "lb":		# Lelf Buttons
		return pygame.joystick.Joystick(0).get_button(4)	
	if button == "rb":		#	Right Buttons
		return pygame.joystick.Joystick(0).get_button(5)	
	if button == "lt":		#	Left Trigger
		return pygame.joystick.Joystick(0).get_button(6)	
	if button == "rt":		# Right Trigger
		return pygame.joystick.Joystick(0).get_button(7)	
	if button == "select":
		return pygame.joystick.Joystick(0).get_button(8)	
	if button == "start":
		return pygame.joystick.Joystick(0).get_button(9)
	if button == "ps":
		return pygame.joystick.Joystick(0).get_button(10)
	if button == "lth":		# left Thumb
		return pygame.joystick.Joystick(0).get_button(11)
	if button == "rth":		# Right Thumb
		return pygame.joystick.Joystick(0).get_button(12)
	if button == "up":
		return pygame.joystick.Joystick(0).get_button(13)
	if button == "down":
		return pygame.joystick.Joystick(0).get_button(14)
	if button == "left":
		return pygame.joystick.Joystick(0).get_button(15)
	if button == "right":
		return pygame.joystick.Joystick(0).get_button(16)
	
	
	