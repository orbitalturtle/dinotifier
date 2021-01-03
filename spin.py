import serial
import time

connected = False

ser = serial.Serial("/dev/ttyACM0")

def move_motor():
    ser.write(b'F')
