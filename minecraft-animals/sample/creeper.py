#!/usr/bin/env python

# Load the required modules and functions
from turtle import *
from random import choice

# Draw a box on screen with a given color
def drawbox(i_color):
	pencolor(i_color)
	fillcolor(i_color)
	begin_fill()
	for i in range(4):
		forward(boxlength)
		left(90)
	end_fill()

# Return to the starting position for a new row
def reset_row():
	left(90)
	forward(boxlength)
	left(90)
	forward(boxlength * 10)
	left(180)

# Get a random green color
def get_color():
	return choice(greens)

# Assign some variables and configure the Turtle environment
def setup():
	# Turtle stuff
	colormode(255)
	hideturtle()
	speed(0)

	# Box Side Length
	global boxlength 
	boxlength = 40

	# Colors
	global greens
	greens  = [[25,160,13]]
	greens += [[91,193,88]]
	greens += [[150,208,138]]
	greens += [[39,142,28]]
	greens += [[95,192,84]]
	greens += [[73,174,61]]

	# Image
	global image
	image  = [[0,0,0,0,0,0,0,0,0,0]]
	image += [[0,0,0,0,0,0,0,0,0,0]]
	image += [[0,0,1,1,0,0,1,1,0,0]]
	image += [[0,0,1,1,0,0,1,1,0,0]]
	image += [[0,0,0,0,1,1,0,0,0,0]]
	image += [[0,0,0,1,1,1,1,0,0,0]]
	image += [[0,0,0,1,1,1,1,0,0,0]]
	image += [[0,0,0,1,0,0,1,0,0,0]]
	image += [[0,0,0,0,0,0,0,0,0,0]]
	image += [[0,0,0,0,0,0,0,0,0,0]]

# Main method. Sets up and draws the image
def main():
	setup()
	image.reverse()
	for row in image:
		for box in row:
			if box == 0:
				drawbox(get_color())
			else:
				drawbox("black")
			forward(boxlength)
		reset_row()

	# Wait to finish
	raw_input()

# Run main
if __name__ == "__main__":
	main()

