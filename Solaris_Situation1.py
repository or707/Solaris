#!/usr/bin/python3
#  -*- coding: utf-8 -*-

# Date: Sat 29 May 2021 19:33:00 CET
# Author: Oriane Cortes
# Description:
# Python Version 3.9
# Last modified: Sun 31 May 2021 19:33:00 CET
# By: Oriane Cortes

import time
import board
import pwmio
from adafruit_motor import servo

pwm1 = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)	#for Servo 1
pwm2 = pwmio.PWMOut(board.A4, duty_cycle=2 ** 15, frequency=50)	#For servo2


servo1 = servo.Servo(pwm1)
servo2 = servo.Servo(pwm2)

while True:
	for angle in range(0, 180, 5):
		servo1.angle = angle
		if angle > 90:
			servo2.angle = 180 - angle
		else:
			servo2.angle = angle
		time.sleep(0.5)