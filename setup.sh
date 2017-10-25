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

