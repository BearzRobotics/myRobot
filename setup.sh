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

# set up firewall
sudo apt install ufw
sudo systemctl enable ufw
sudo systemctl start ufw

# Allows port 1150 and 1110
sudo ufw allow 1150/udp
sudo ufw allow 1110/udp

# installs python libs
sudo pip3 install pyfrc pygame psutils pypacker

# setup Mdns
sudo apt install avahi-daemon

# Setup rc.locol
sudo cp -apr /etc/rc.locol to rc-locol.bak
sudo rm /etc/rc.locol
sudo echo "#!/bin/sh -e" >> /etc/rc.locol
sudo echo "#" >> /etc/rc.locol
sudo echo "# rc.local" >> /etc/rc.locol
sudo echo "#" >> /etc/rc.locol
sudo echo "# This script is executed at the end of each multiuser runlevel." >> /etc/rc.locol
sudo echo "# Make sure that the script will "exit 0" on success or any other" >> /etc/rc.locol
sudo echo "# value on error." >> /etc/rc.locol
sudo echo "#" >> /etc/rc.locol
sudo echo "# In order to enable or disable this script just change the execution" >> /etc/rc.locol
sudo echo "# bits." >> /etc/rc.locol
sudo echo "#" >> /etc/rc.locol
sudo echo "# By default this script does nothing." >> /etc/rc.locol
sudo echo "" >> /etc/rc.locol
sudo echo "# Print the IP address" >> /etc/rc.locol
sudo echo "_IP=$(hostname -I) || true" >> /etc/rc.locol
sudo echo "if [ "$_IP" ]; then" >> /etc/rc.locol
sudo echo "  printf "My IP address is %s\n" "$_IP"" >> /etc/rc.locol
sudo echo "fi" >> /etc/rc.locol
sudo echo "" >> /etc/rc.locol
sudo echo "sudo python3 /home/pi/myRobot/src/status.py &" >> /etc/rc.locol
sudo echo "" >> /etc/rc.locol
sudo echo "exit 0" >> /etc/rc.locol

