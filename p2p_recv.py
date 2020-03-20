import time
import serial
import sys
import socket

BAUDRATE=57600

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 6688

client.connect((host,port))
input = raw_input
serial_port = input("Serial Port ? ")

lora = serial.Serial(serial_port, BAUDRATE)

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

lora.write(b'mac pause\r\n')
lora.readline()

try:
    while True:

        lora.write(b'radio rx 0\r\n')

        if lora.readline().strip() == "ok" or "radio_tx_ok" :            
            raw = str(lora.readline().strip())
            if raw.startswith('radio_rx'):
                print('----------------------------------')
                ts = str(time.time())
                data = raw.split(' ', 2)
                payload = data[2].decode("hex")
                client.sendall(str(payload))
                print(payload + ts)

finally:
    if lora is not None:
        lora.close()
