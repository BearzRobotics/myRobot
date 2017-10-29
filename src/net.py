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

import socket
import time
Server = '192.168.1.68' # Hard coded for now

def writeNc(Message):
	Wn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	Port = 6666
	Wn.connect((Server, Port))
	Wn.sendto(str(Message).encode('utf-8'), (Server, Port))
	Wn.close()

def writeStatus(Message):
	Ws = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	Port = 7000
	StatusServer = '127.0.0.1'
	Ws.connect((StatusServer, Port))
	Ws.sendto(str(Message).encode('utf-8'), (StatusServer, Port))
	Ws.close()

class ds:
	def __init__(self):
		pass
		
		
	def readDs():
		# socket.AF_INET, allows use of ipv4
		# socket.SOCK_STREAM use tcp packets
		# socket.SOCK_DGRAM use udp
		R = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		Port = 1110
		R.bind(('', Port))
		R.settimeout(100000)
		while True:
				data, addr = R.recvfrom(4096)
				data = data.decode('utf-8')
				if not data:
					break
				return data
		R.close()

	def writeDs(Message):
		W = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		Port = 1150
		W.connect((Server, Port))
		W.sendto(str(Message).encode('utf-8'), (Server, Port))
		W.close()

def mode():
	mode = ds.readDs()
	#print(mode)
	return mode	
