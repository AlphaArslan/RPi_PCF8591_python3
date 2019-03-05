import time
from smbus2 import SMBus

address = 0x48
A0      = 0x40
A1	= 0x41
A2	= 0x42
A3	= 0x43

bus = SMBus(1)

while True:
	bus.write_byte(address, A0)
	value = bus.read_byte(address)
	if(value<3):
		print("- No Pressure")
	elif(value<50):
		print("- Light Touch")
	elif(value<125):
		print("- Light Squeeze")
	elif(value<200):
		print("- Meduim Squeeze")
	else:
		print("- Big Squeeze")
	time.sleep(1)
