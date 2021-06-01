#!/usr/bin/python3
#  -*- coding: utf-8 -*-

# Date: Sat 29 May 2021 22:12:00 CET
# Author: Oriane Cortes
# Description:
# Python Version 3.9
# Last modified: Sun 31 May 2021 19:50:00 CET
# By: Oriane Cortes


import time
import board
import pwmio
from adafruit_motor import servo
from adafruit_circuitplayground.express import cpx	# To use the CPX light module - use another library for the prototype

pwm_rot = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)	# for Servo 1
pwm_incl = pwmio.PWMOut(board.A4, duty_cycle=2 ** 15, frequency=50)	# For servo 2


servo_rot = servo.Servo(pwm_rot)
servo_incl = servo.Servo(pwm_incl)

def move_servo(s, Step):
	'''
	Fonction that move the servo 1 or 2 at the angle chosen.
	Use: move_servo(x, y) x = the number of the servo and y = the angle. 
	'''
	global servo_rot
	global servo_incl
	if s = 1:
		servo_rot.angle = Step
	else: 
		servo_incl.angle = Step

def change(LT, LB, RT, RB):
	'''
	Fonction that define in wich direction the servos needs to move.
	'''
	LT=cpx.light	# need to be adapted 
	LB=cpx.light	# to the commands of 
	RT=cpx.light	# the light sensor
	RB=cpx.light	# of the prototype

	Step_rot = 5	# in °, need to change the sign if for 180° the solar panel's attitude is on the left
	Step_incl = 5	# in °, need to change the sign if for 180° the solar panel's attitude is on the the very bottom 
	if LT and LB < (max(LT, lB, RT, RB)) / 2:
		move_servo(1, Step_rot)
	elif RT and RB < (max(LT, lB, RT, RB)) / 2:
		move_servo(1, -Step_rot)
	elif RT and LT < (max(LT, lB, RT, RB)) / 2:
		move_servo(2, -Step_incl)
	elif LB and RB < (max(LT, lB, RT, RB)) / 2:
		move_servo(2, Step_incl)
	else:
		pass

while True:
	change()
