# gpsdtoaprs
Parses GPS data from GPSD to APRS-friendly format. gpsd-py3 Python package needed. Defines functions to return latitude and longitude in format for broadcast in APRS position packet.<br><br>
Requirements:<br>
sudo apt-get install gpsd gpsd-clients<br>
pip3 install gpsd-py3<br><br>
How to setup GPSD to receive UDP packet:<br>
sudo systemctl stop gpsd<br>
sudo systemctl stop gpsd.socket<br>
sudo nano /etc/default/gpsd<br>
comment line starting DEVICES and insert below:<br>
DEVICES="udp://[YOUR_RASPBERRY_PI_IP]:[YOUR_SELECTED_PORT]" (eg. DEVICES="udp://10.0.0.1:11123")<br>
Save the file<br>
sudo systemctl enable gpsd<br>
sudo systemctl enable gpsd.socket<br>
Reboot, and GPSD should from startup listen at the port set for GPS packets<br>
Run "cgps" to see the dashboard<br>
