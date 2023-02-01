# Read the serial port data from the COM3 
import serial 

ser = serial.Serial('COM3', 921600)
ser.baudrate = 921600
ser.port = 'COM3'
ser.open()
print('com3 is open', ser.isOpen())