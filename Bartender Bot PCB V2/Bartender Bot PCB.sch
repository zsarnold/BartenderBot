EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Interface_Expansion:MCP23017_SO U1
U 1 1 5FC5ECEE
P 4850 2100
F 0 "U1" H 4350 3300 50  0000 C CNN
F 1 "MCP23017_SO" H 4400 3200 50  0000 C CNN
F 2 "Package_SO:SOIC-28W_7.5x17.9mm_P1.27mm" H 5050 1100 50  0001 L CNN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/20001952C.pdf" H 5050 1000 50  0001 L CNN
	1    4850 2100
	1    0    0    -1  
$EndComp
$Comp
L Connector:Screw_Terminal_01x04 J3
U 1 1 5FC60520
P 1500 1150
F 0 "J3" H 1650 1150 50  0000 C CNN
F 1 "Screw_Terminal_01x04" H 2000 1050 50  0000 C CNN
F 2 "TerminalBlock_Phoenix:TerminalBlock_Phoenix_MPT-0,5-4-2.54_1x04_P2.54mm_Horizontal" H 1500 1150 50  0001 C CNN
F 3 "~" H 1500 1150 50  0001 C CNN
	1    1500 1150
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR07
U 1 1 5FC62FDC
P 850 1050
F 0 "#PWR07" H 850 900 50  0001 C CNN
F 1 "+5V" H 865 1223 50  0000 C CNN
F 2 "" H 850 1050 50  0001 C CNN
F 3 "" H 850 1050 50  0001 C CNN
	1    850  1050
	-1   0    0    -1  
$EndComp
$Comp
L Connector:Screw_Terminal_01x04 J4
U 1 1 5FC6A709
P 1500 1650
F 0 "J4" H 1650 1650 50  0000 C CNN
F 1 "Screw_Terminal_01x04" H 2000 1550 50  0000 C CNN
F 2 "TerminalBlock_Phoenix:TerminalBlock_Phoenix_MPT-0,5-4-2.54_1x04_P2.54mm_Horizontal" H 1500 1650 50  0001 C CNN
F 3 "~" H 1500 1650 50  0001 C CNN
	1    1500 1650
	1    0    0    -1  
$EndComp
$Comp
L Connector:Screw_Terminal_01x04 J5
U 1 1 5FC6AE87
P 1500 2150
F 0 "J5" H 1650 2150 50  0000 C CNN
F 1 "Screw_Terminal_01x04" H 2000 2050 50  0000 C CNN
F 2 "TerminalBlock_Phoenix:TerminalBlock_Phoenix_MPT-0,5-4-2.54_1x04_P2.54mm_Horizontal" H 1500 2150 50  0001 C CNN
F 3 "~" H 1500 2150 50  0001 C CNN
	1    1500 2150
	1    0    0    -1  
$EndComp
$Comp
L Connector:Screw_Terminal_01x04 J6
U 1 1 5FC6C712
P 1500 2650
F 0 "J6" H 1650 2650 50  0000 C CNN
F 1 "Screw_Terminal_01x04" H 2000 2550 50  0000 C CNN
F 2 "TerminalBlock_Phoenix:TerminalBlock_Phoenix_MPT-0,5-4-2.54_1x04_P2.54mm_Horizontal" H 1500 2650 50  0001 C CNN
F 3 "~" H 1500 2650 50  0001 C CNN
	1    1500 2650
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR08
U 1 1 5FC72933
P 850 1150
F 0 "#PWR08" H 850 900 50  0001 C CNN
F 1 "GND" H 855 977 50  0000 C CNN
F 2 "" H 850 1150 50  0001 C CNN
F 3 "" H 850 1150 50  0001 C CNN
	1    850  1150
	-1   0    0    -1  
$EndComp
Text Label 1150 2750 2    50   ~ 0
SDA
Text Label 1150 2850 2    50   ~ 0
SCK
Text Label 4000 1300 2    50   ~ 0
SDA
Text Label 4000 1400 2    50   ~ 0
SCK
Wire Wire Line
	4000 1300 4150 1300
Wire Wire Line
	4000 1400 4150 1400
Wire Wire Line
	1300 2750 1150 2750
Wire Wire Line
	1150 2850 1300 2850
$Comp
L power:+5V #PWR01
U 1 1 5FC7D76D
P 2850 950
F 0 "#PWR01" H 2850 800 50  0001 C CNN
F 1 "+5V" H 2750 1050 50  0000 C CNN
F 2 "" H 2850 950 50  0001 C CNN
F 3 "" H 2850 950 50  0001 C CNN
	1    2850 950 
	1    0    0    -1  
$EndComp
$Comp
L power:+12V #PWR05
U 1 1 5FC7E27E
P 2850 1150
F 0 "#PWR05" H 2850 1000 50  0001 C CNN
F 1 "+12V" V 2950 1250 50  0000 C CNN
F 2 "" H 2850 1150 50  0001 C CNN
F 3 "" H 2850 1150 50  0001 C CNN
	1    2850 1150
	-1   0    0    1   
$EndComp
Wire Wire Line
	3000 950  2850 950 
$Comp
L power:GND #PWR04
U 1 1 5FC82AB4
P 2600 1100
F 0 "#PWR04" H 2600 850 50  0001 C CNN
F 1 "GND" H 2605 927 50  0000 C CNN
F 2 "" H 2600 1100 50  0001 C CNN
F 3 "" H 2600 1100 50  0001 C CNN
	1    2600 1100
	1    0    0    -1  
$EndComp
Wire Wire Line
	2600 1050 2600 1100
Wire Wire Line
	2600 1050 3000 1050
$Comp
L power:+5V #PWR02
U 1 1 5FC89705
P 4850 950
F 0 "#PWR02" H 4850 800 50  0001 C CNN
F 1 "+5V" H 4750 1050 50  0000 C CNN
F 2 "" H 4850 950 50  0001 C CNN
F 3 "" H 4850 950 50  0001 C CNN
	1    4850 950 
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR09
U 1 1 5FC89CF0
P 4850 3300
F 0 "#PWR09" H 4850 3050 50  0001 C CNN
F 1 "GND" H 4855 3127 50  0000 C CNN
F 2 "" H 4850 3300 50  0001 C CNN
F 3 "" H 4850 3300 50  0001 C CNN
	1    4850 3300
	1    0    0    -1  
$EndComp
Wire Wire Line
	850  1050 1300 1050
Wire Wire Line
	4850 950  4850 1000
Text Label 5600 1300 0    50   ~ 0
Pump1
Text Label 5600 1400 0    50   ~ 0
Pump2
Text Label 5600 1500 0    50   ~ 0
Pump3
Text Label 5600 1600 0    50   ~ 0
Pump4
Text Label 5600 1700 0    50   ~ 0
Pump5
Text Label 5600 1800 0    50   ~ 0
Pump6
Text Label 5600 1900 0    50   ~ 0
Pump7
Text Label 5600 2000 0    50   ~ 0
Pump8
Wire Wire Line
	5600 1300 5550 1300
Wire Wire Line
	5550 1400 5600 1400
Wire Wire Line
	5600 1500 5550 1500
Wire Wire Line
	5550 1600 5600 1600
Wire Wire Line
	5600 1700 5550 1700
Wire Wire Line
	5550 1800 5600 1800
Wire Wire Line
	5600 1900 5550 1900
Wire Wire Line
	5550 2000 5600 2000
Text Label 1250 1550 2    50   ~ 0
Pump1
Text Label 1250 1650 2    50   ~ 0
Pump2
Text Label 1250 1750 2    50   ~ 0
Pump3
Text Label 1250 1850 2    50   ~ 0
Pump4
Text Label 1250 2050 2    50   ~ 0
Pump5
Text Label 1250 2150 2    50   ~ 0
Pump6
Text Label 1250 2250 2    50   ~ 0
Pump7
Text Label 1250 2350 2    50   ~ 0
Pump8
Wire Wire Line
	1250 1550 1300 1550
Wire Wire Line
	1300 1650 1250 1650
Wire Wire Line
	1250 1750 1300 1750
Wire Wire Line
	1300 1850 1250 1850
Wire Wire Line
	1250 2050 1300 2050
Wire Wire Line
	1300 2150 1250 2150
Wire Wire Line
	1250 2250 1300 2250
Wire Wire Line
	1300 2350 1250 2350
Text Label 5600 2200 0    50   ~ 0
StepA
Text Label 5600 2300 0    50   ~ 0
StepB
Wire Wire Line
	5600 2200 5550 2200
Wire Wire Line
	5600 2300 5550 2300
Text Label 1200 2550 2    50   ~ 0
StepA
Text Label 1200 2650 2    50   ~ 0
StepB
Wire Notes Line
	3800 1400 2450 1400
Wire Notes Line
	5900 750  5900 3600
Wire Notes Line
	5900 3600 3800 3600
Wire Notes Line
	2450 750  2450 3050
Wire Notes Line
	750  3050 750  750 
Text Notes 750  750  0    50   ~ 0
Screw Terminal Outputs to Pi\n
Text Notes 2450 750  0    50   ~ 0
5V Regulator Header
Wire Notes Line
	3800 750  3800 3600
Text Notes 3800 750  0    50   ~ 0
IO Expander
NoConn ~ 5550 2400
NoConn ~ 5550 2500
NoConn ~ 5550 2600
NoConn ~ 5550 2700
NoConn ~ 5550 2800
NoConn ~ 5550 2900
NoConn ~ 4150 2000
NoConn ~ 4150 1900
Wire Wire Line
	4150 2800 4150 2900
Wire Wire Line
	4150 2700 4150 2800
Connection ~ 4150 2800
$Comp
L power:+5V #PWR0101
U 1 1 5FCE51EF
P 4000 2100
F 0 "#PWR0101" H 4000 1950 50  0001 C CNN
F 1 "+5V" H 3900 2200 50  0000 C CNN
F 2 "" H 4000 2100 50  0001 C CNN
F 3 "" H 4000 2100 50  0001 C CNN
	1    4000 2100
	1    0    0    -1  
$EndComp
Wire Wire Line
	4000 2100 4000 2200
Wire Wire Line
	4000 2200 4150 2200
Wire Wire Line
	4850 3200 4850 3300
$Comp
L power:GND #PWR0102
U 1 1 5FCE6FAB
P 4150 3050
F 0 "#PWR0102" H 4150 2800 50  0001 C CNN
F 1 "GND" H 4155 2877 50  0000 C CNN
F 2 "" H 4150 3050 50  0001 C CNN
F 3 "" H 4150 3050 50  0001 C CNN
	1    4150 3050
	1    0    0    -1  
$EndComp
Wire Wire Line
	4150 3050 4150 2900
Connection ~ 4150 2900
Wire Notes Line
	750  3050 2450 3050
Wire Wire Line
	1200 2550 1300 2550
Wire Wire Line
	1200 2650 1300 2650
$Comp
L power:+12V #PWR0103
U 1 1 5FCF320C
P 1000 1350
F 0 "#PWR0103" H 1000 1200 50  0001 C CNN
F 1 "+12V" H 1100 1450 50  0000 C CNN
F 2 "" H 1000 1350 50  0001 C CNN
F 3 "" H 1000 1350 50  0001 C CNN
	1    1000 1350
	1    0    0    -1  
$EndComp
Wire Wire Line
	1000 1350 1300 1350
Wire Wire Line
	850  1150 1250 1150
Wire Wire Line
	1300 1250 1250 1250
Wire Wire Line
	1250 1250 1250 1150
Connection ~ 1250 1150
Wire Wire Line
	1250 1150 1300 1150
Wire Notes Line
	750  750  5900 750 
Wire Wire Line
	2850 1150 3000 1150
$Comp
L Connector_Generic:Conn_01x04 J1
U 1 1 5FC7B180
P 3200 1050
F 0 "J1" H 3280 1042 50  0000 L CNN
F 1 "Conn_01x04" H 3280 951 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical" H 3200 1050 50  0001 C CNN
F 3 "~" H 3200 1050 50  0001 C CNN
	1    3200 1050
	1    0    0    -1  
$EndComp
NoConn ~ 3000 1250
$EndSCHEMATC
