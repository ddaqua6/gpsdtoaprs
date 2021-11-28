# gpsdtoaprs
Parses GPS data from GPSD to APRS-friendly format. gpsd-py3 Python package needed. Defines functions to return latitude and longitude in format for broadcast in APRS position packet.<br><br>
Requirements:<br>
sudo apt-get install gpsd gpsd-clients<br>
pip3 install gpsd-py3<br><br>
How to setup GPSD to receive UDP packet:<br>
sudo systemctl stop gpsd<br>
sudo systemctl stop gpsd.socket<br>
gpsd -N udp://[RASPBERRY_IP]:[YOUR_DESIGNED_PORT] (eg. gpsd -N udp://10.0.0.1:8000)<br>
sudo systemctl enable gpsd<br>
sudo systemctl enable gpsd.socket<br>
Reboot, and GPSD should from startup listen at the port set for GPS packets
