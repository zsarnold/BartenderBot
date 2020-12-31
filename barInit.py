#BartenderBotV0
#https://github.com/zsarnold
#Test file. Used to intialize I2C I/O expander at raspi boot.

import smbus

#I2C setup
bus = smbus.SMBus(1)

DEVICE = 0x20
IODIRA = 0x00
OLATA  = 0x14
GPIOA  = 0x12
IODIRB = 0x01
OLATB  = 0x15
GPIOB  = 0x13

#Set GPA pins to output
bus.write_byte_data(DEVICE, IODIRB, 0x00)
bus.write_byte_data(DEVICE, IODIRA, 0x00)

#Set all ports to 0
bus.write_byte_data(DEVICE, OLATB, 0)
bus.write_byte_data(DEVICE, OLATA, 0)
