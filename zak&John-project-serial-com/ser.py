import serial

ser = serial.Serial('/dev/ttyUSB0')  # This format is specific to Debian Linux environments
print(ser.name)          # check which port was really used
ser.write('hello\n')     # write a string
ser.close()              # close port

ser = serial.Serial('COM3', 38400, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)
s = ser.read(100)       # read up to one hundred bytes
ser.close()              # close port