# myRobot
This is meant to work with (qdriverstation)[https://github.com/FRC-Utilities/QDriverStation]. 

This is a simple robot project written in python 3.

Basic program structure is to have 2 main opertion modes. The first being a Telo and the second automimous. The defualt will be the telo.
The program asumes that the user running it has access to its home dir '~'. The program becomes on gaint while loop. I know this is bad for most
things, but for this it should be fine. Defs and Class shell start with a lowercase and conform to camel case there after. Varables shall start 
wtih a capital and shall conform to camel case there affer. 

Example:
def: writeCode()
var: RedLed

One of the goals is to get this to work with the qdriverstation both the desktop and phone version. This will allow the robot to be controlled
from a windows, mac, Linux, bsd, android phone or other operating system that can compile qt version 5.
=======================================Configure reboot=========================================
This allows anyone in the wheel group to shutdown the computer with out super user. They still
need to put sudo infront of the command tho.
copy bellow lines into '/etc/group'

%wheel ALL= NOPASSWD: /sbin/shutdown
%wheel ALL= NOPASSWD: /sbin/reboot

 -- or --
 chmod both to be 6777 to allow non sudo users to acces them 
=======================================Adb File (Format)=========================================
X joystick value | Y joystick value | z joystick value | Button 1 | Button 2 | Button 3 | Button 4
--------------------------------------------------------------------------------------------------
1 through -1	 | 1 through -1     | 1 through -1     | T or F   | T or F   | T or F   | T or F

=======================================Competetion rules=======================================
Rules:
Auton: First 20 secs
Telo: 3 minutes




=======================================Complaints agains python ==============================

There needs to be something like cargo doc, becaue after using rust, I've grown accustom to putting so much info into comments around my code.
I wonder will this slow python down?

======================================= Sources ==============================================

https://pythonhosted.org/triangula/config.html


- I used this for ps3 blutooth support
	https://github.com/DexterInd/GoPiGo

- This adds smart dashboard 
	https://github.com/robotpy/pynetworktables

- This is the dashboard used. Its written in java and can be run anywhere java can.
	https://github.com/wpilibsuite/SmartDashboard

- This adds netconsle support
	https://github.com/robotpy/pynetconsole

- Mdns
	https://www.howtogeek.com/167190/how-and-why-to-assign-the-.local-domain-to-your-raspberry-pi/

- CPU/Ram
	https://pypi.python.org/pypi/psutil
