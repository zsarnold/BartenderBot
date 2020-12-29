#BartenderBotV0
#https://github.com/zsarnold
#Pump file. Used to control pumps for certain time.

import smbus
import time

#I2C setup
bus = smbus.SMBus(1)

DEVICE = 0x20
IODIRB = 0x01
OLATB  = 0x15
GPIOB  = 0x13

#Set GPA pins to output
bus.write_byte_data(DEVICE, IODIRB, 0x00)

#Set all ports to 0
bus.write_byte_data(DEVICE, OLATB, 0)


def pump( pumpNum, time ):
    #set pump high
    bus.write_byte_data(DEVICE, OLATB, pumpNum)
    #wait the time
    time.sleep(time)
    #set pump low
    bus.write_byte_data(DEVICE, OLATB, 0)
