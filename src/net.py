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
from struct import * # interpret bytes as packed binary data
import time
Server = '192.168.1.68' # Hard coded for now
# Raw bytes for the FRC_2015 protocol
Test               = 0x01;
Enabled            = 0x04;
Autonomous         = 0x02;
Teleoperated       = 0x00;
FMS_Attached       = 0x08;
EmergencyStop      = 0x80;
RequestReboot      = 0x08;
RequestNormal      = 0x80;
RequestUnconnected = 0x00;
RequestRestartCode = 0x04;
FMS_RadioPing      = 0x10;
FMS_RobotPing      = 0x08;
FMS_RobotComms     = 0x20;
FMS_DS_Version     = 0x00;
TagDate            = 0x0f;
TagGeneral         = 0x01;
TagJoystick        = 0x0c;
TagTimezone        = 0x10;
Red1               = 0x00;
Red2               = 0x01;
Red3               = 0x02;
Blue1              = 0x03;
Blue2              = 0x04;
Blue3              = 0x05;
RTagCANInfo        = 0x0e;
RTagCPUInfo        = 0x05;
RTagRAMInfo        = 0x06;
RTagDiskInfo       = 0x04;
RequestTime        = 0x01;
RobotHasCode       = 0x20;

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
		Port = 7110
		R.bind(('', Port))
		R.settimeout(100000)
		while True:
				data, addr = R.recvfrom(4096)
				if not data:
					break
				return data
		R.close()
	#Bt stands for Button then the number ofthe controller appaned to it. 
	#	-- Returns a true or false
	#Ax stands for joystick Axis
	#	-- Returns a flout of the joystick or other axis
	#This protocol jupports 16 buttons and 5 axis at the most. The defualt value is null resulting in a null byte being sent
	def writeDs(ControlByte, Direction=None, Bt1=None, Bt2=None, Bt3=None, Bt4=None, Bt5=None, Bt6=None, Bt7=None, Bt8=None, Bt9=None, Bt10=None, Bt11=None, Bt12=None, Bt13=None, Bt14=None, Bt15=None, B1t6=None, Ax1=None, Ax3=None, Ax3=None, Ax4=None, Ax5=None ):
		W = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		Port = 7150
		W.connect((Server, Port))
		
		# For format refer back to https://docs.python.org/3.0/library/struct.html
		# For debug we'll print our new data
		print(ControlByte, Direction, Bt1, Bt2, Bt3, Bt4, Bt5, Bt6, Bt7, Bt8, Bt9, Bt10, Bt11, Bt12, Bt13, Bt14, Bt15, B1t6, Ax1, Ax3, Ax3, Ax4, Ax5)
		
		# Format-	C Type	-	Python type	-	Standard Size
		# c			char	    str len of 1			1
		# ?			bool		bool					1
		# f			float		float					4
		
		data = pack('cc????????????????fffff', ControlByte, Direction, Bt1, Bt2, Bt3, Bt4, Bt5, Bt6, Bt7, Bt8, Bt9, Bt10, Bt11, Bt12, Bt13, Bt14, Bt15, B1t6, Ax1, Ax3, Ax3, Ax4, Ax5)
		W.sendto(data, (Server, Port))
		W.close()


def mode():
	mode = ds.readDs()
	#print(mode)
	return mode	
	
class frc_2015:
	def decryptPacket():
		DSP = ds.readDs()
		print(DSP)
		DECP = unpack("!Ih", DSP)[0]  # DECP means De-encrypted Packet
		print(DECP)
		
#frc_2015.decryptPacket()		
