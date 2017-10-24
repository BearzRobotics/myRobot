import linecache
import time

def writeCode():
	Adb = open('./adb', 'a')
	Adb.write("This is a tesst")

	Adb.close()

def readCode():
	count = 1
	
	BegingLine = count + 1	
	linecache.getline('./adb', BegingLine)

	linecache.clearcache()
