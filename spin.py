import serial

connected = False

ser = serial.Serial("/dev/ttyACM0", 9600)

ser.write(b'F')

ser.close()
