#!/usr/bin/python

from turtle import *

colormode(255)

endermangrey = [22, 22, 22]

def colorsquare(input_color):
	
	pencolor(input_color)
	
	fillcolor(input_color)

	begin_fill()

	for i in range (4):

		forward(100)

		left(90)

	end_fill()

speed(0)

penup()

left(180)

forward(400)

right(90)

forward(400)

pendown()

row_1 = ["black",endermangrey,"black","black","black","black",endermangrey,"black"]

for color in row_1:
	colorsquare(color)
	forward(100)

raw_input()