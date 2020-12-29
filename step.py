#BartenderBotV0
#https://github.com/zsarnold
#stepper file. Used to control the stepper motor

import smbus
import time

#I2C setup
bus = smbus.SMBus(1)

DEVICE = 0x20
IODIRA = 0x00
OLATA  = 0x14
GPIOA  = 0x12

#Set GPA pins to output
bus.write_byte_data(DEVICE, IODIRA, 0x00)

#Set all ports to 0
bus.write_byte_data(DEVICE, OLATA, 0)

#pin assignments
A1 =
A2 =
B1 =
B2 =

def step(stepVal):
    if stepVal == 0:
        A1.value = True
        A2.value = False
        B1.value = True
        B2.value = False
    elif stepVal == 1:
        A1.value = False
        A2.value = True
        B1.value = True
        B2.value = False
    elif stepVal == 2:
        A1.value = False
        A2.value = True
        B1.value = False
        B2.value = True
    elif stepVal == 3:
        A1.value = True
        A2.value = False
        B1.value = False
        B2.value = True

def stepFWD( numSteps ):
    for s in range(numSteps):
        i = s % 4
        # step motor
        step(i)
        time.sleep(0.01)

def stepBWD( numSteps ):
