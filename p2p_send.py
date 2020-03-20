import serial
import time
import sys

BAUDRATE = 57600
input = raw_input
#lora serial port
serial_port = input("Serial Port ? ")
#sensor data file
filename = input("File name ? ")

lora = serial.Serial(serial_port, BAUDRATE)
#lora = serial.Serial("/dev/ttyACM0", 57600)

lora.write(b'radio cw off\r\n')
lora.readline()
# bw=125
lora.write(b'radio set bw 125\r\n')
lora.readline()
# pwr=15
lora.write(b'radio set pwr 15\r\n')
lora.readline()
# sf=sf12
lora.write(b'radio set sf sf12\r\n')
lora.readline()
# freq=868100000
lora.write(b'radio set freq 868100000\r\n')
print(str(lora.readline()))


while True:
    lora.write(b'mac pause\r\n')
    lora.readline()
        
    file = open(filename, 'r')
    fileinput = file.readline()
    print(fileinput)
    data = fileinput.encode("hex")

    cmd ='radio tx ' + data + '\r\n'
    #print(cmd)

    payload = bytes(cmd)
    lora.write(payload)
    lora.readline()
    time.sleep(10)
