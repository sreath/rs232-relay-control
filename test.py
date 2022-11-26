import serial
import time

port = '/dev/ttyUSB0'
baudrate = 9600
serialPort = serial.Serial(port=port, baudrate=baudrate,
                                bytesize=8, timeout=1, 
stopbits=serial.STOPBITS_ONE)
while True:
	serialPort.setRTS(False)
	print("rts False")
	time.sleep(3)
	serialPort.setRTS(True)
	print("rts True")
	time.sleep(3)
