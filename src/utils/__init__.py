#!/usr/bin/python3
import os
import psutil


def reboot():
	os.system("/sbin/reboot")
	psutil.disk_usage('/')
	
def getRam():
	psutil.virtual_memory()
	
def getCpu():
	psutil.cpu_freq()

def diskUsage():
	psutil.disk_usage('/')
