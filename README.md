# myRobot
This is meant to work with [driverstation](https://github.com/BearzRobotics/DriverStation). 

This is a simple robot project written in python 3.

Basic program structure is to have 2 main opertion modes. The first being a Telo and the second automimous.
The defualt will be the telo. The program asumes that the user running it has access to its home dir '~'. 
The program becomes on gaint while loop. I know this is bad for most things, but for this it should be fine.
Defs and Class shell start with a lowercase and conform to camel case there after. Varables shall start 
wtih a capital and shall conform to camel case there affer. 

Example:
def: writeCode()
var: RedLed

**Status LED Program:**
This needs to be started at system boot. (refer to rc.locol) Make sure the procces is forked.  

The program will read for the change at port 7000 and if nessary write on port 7001.
Read = 7000
Write = 7001


**Configure reboot:**
This allows anyone in the wheel group to shutdown the computer with out super user. They still
need to put sudo infront of the command tho.
copy bellow lines into '/etc/group'

%wheel ALL= NOPASSWD: /sbin/shutdown
%wheel ALL= NOPASSWD: /sbin/reboot

   or
 chmod both to be 6777 to allow non sudo users to acces them

 
**Adb File (Format):**
X joystick value | Y joystick value | z joystick value | Button 1 | Button 2 | Button 3 | Button 4
--------------------------------------------------------------------------------------------------
1 through -1	 | 1 through -1     | 1 through -1     | T or F   | T or F   | T or F   | T or F


**Competetion rules:**
Auton: First 20 secs
Telo: 3 minutes


**Complaints agains python:** 
There needs to be something like cargo doc, becaue after using rust, I've grown accustom to putting so 
much info into comments around my code. I wonder will this slow python down?


**NET:**
IF using wifi, it must have a connection at startup.
adding this to /etc/network/interfaces should make it work

auto wlan0
iface wlan0 inet dhcp
        wpa-ssid "ssid"
        wpa-psk "password"


**rc.local:**
We need to edit rc.local to get are program to start up with the system
sudo nano /etc/rc.local

put in the program you wish to have start up. For us it is status.py
/home/pi/myRobot/src/status.py
if the program is likely to run in a infinate loop or not exit put '&' and the end to fork the
process.
/home/pi/myRobot/src/status.py &

**Custom Packet**
ccc?????????????????ffffff
Feilds for DECP are 0 -25
This is the table if you wanted to pull a spesific byte
c	mode			DECP[0]			T for telo, A for auton						1
?	Bt0				DECP[1]			T/F											1
?	Bt1				DECP[2]			T/F											1
?	Bt2				DECP[3]			T/F											1
?	Bt3				DECP[4]			T/F											1
?	Bt4				DECP[5]			T/F											1
?	Bt5				DECP[6]			T/F											1
?	Bt6				DECP[7]			T/F											1
?	Bt7				DECP[8]			T/F											1
?	Bt8				DECP[9]			T/F											1
?	Bt9				DECP[10]		T/F											1
?	Bt10			DECP[11]		T/F											1
?	Bt11			DECP[12]		T/F											1
?	Bt12			DECP[13]		T/F											1
?	Bt13			DECP[14]		T/F											1
?	Bt14			DECP[15]		T/F											1
?	Bt15			DECP[16]		T/F											1
?	Bt16			DECP[17]		T/F											1
f	Ax0				DECP[18]		Float										4
f	Ax1				DECP[19]		Float										4
f	Ax2				DECP[20]		Float										4
f	Ax3				DECP[21]		Float										4
f	Ax4				DECP[22]		Float										4
f	Ax5				DECP[23]		Float										4
 															    Packet size ~=	42

**Sources:**
https://pythonhosted.org/triangula/config.html


- I used this for ps3 blutooth support
	https://github.com/DexterInd/GoPiGo

- Mdns
	https://www.howtogeek.com/167190/how-and-why-to-assign-the-.local-domain-to-your-raspberry-pi/

- CPU/Ram
	https://pypi.python.org/pypi/psutil
	
