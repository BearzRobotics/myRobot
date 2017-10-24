#!/usr/bin/python3
import socket

Server = '192.168.1.68' # Hard coded for now
# protocol bytes for parsing
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

def readDs():
	# socket.AF_INET, allows use of ipv4
	# socket.SOCK_STREAM use tcp packets
	# socket.SOCK_DGRAM use udp
	R = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	Port = 1110
	#R.connect((Server, Port))
	R.bind(('', Port))	
	R.settimeout(5)
	while True:
		data, addr = R.recvfrom(4096)
		#data = data.decode('utf-8')		
		if not data:
			break
		print(data)
	R.close()

def writeDs(Message):
	W = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	Port = 1150
	W.connect((Server, Port))
	W.sendto(str(Message).encode('utf-8'), (Server, Port))
	W.close()

readDs()

