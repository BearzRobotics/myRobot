#!/usr/bin/python3
import socket

def readDs():
	# socket.AF_INET, allows use of ipv4
	# socket.SOCK_STREAM use tcp packets
	# socket.SOCK_DGRAM use udp
	R = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#Server = '127.0.0.1'
	#Port = 1150
	
	Server = '192.168.1.68'
	Port = 80

	Request = "GET " +Server+ "\n\n"

	R.connect((Server, Port))
	R.send(Request.encode())
	Result = R.recv(1024)

	print(Result)

def writeDs():
	# socket.AF_INET, allows use of ipv4
	# socket.SOCK_STREAM use tcp packets
	R = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	Server = '127.0.0.1'
	Port = 1110

	Request = "GET " +Server+ "\n\n"

	R.connect((Server, Port))
	R.send(Request.encode())
	Result = R.recv(4096)

	print(Result)

readDs()
