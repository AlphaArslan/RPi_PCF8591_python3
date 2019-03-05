# RPi_PCF8591_python3_FSR
Read analog values with help of PCF8591 module, I2C protocol and python script.
Here we put it into action using simple FSR sensor

# Pin Connection
	======= Raspberry ================== PCF8591 =======
	=======   GPIO2   ----------------->   SDA   =======
	=======   GPIO3   ----------------->   SCL   =======

# Enable I2C Interface
	sudo raspi-config
	Go to Interfacing Options
	Choose I2C and Enable it

# prerequisites
	sudo pip3 install smbus2

# Run Script
	sudo python3 ReadAnalog.py
