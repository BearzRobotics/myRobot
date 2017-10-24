# set up firewall
sudo apt install ufw
sudo systemctl enable ufw
sudo systemctl start ufw

# Allows port 1150 and 1110
sudo ufw allow 1150/udp
sudo ufw allow 1110/udp

# installs python libs
sudo pip3 install pyfrc

# setup Mdns
sudo apt install avahi-daemon

