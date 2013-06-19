#!/usr/bin/python

# Load module
from turtle import *

# Say hello
print "Hello!"

# Define a custom color
chartreuse = [1, 132, 3]

# Make turtle use 0-255 rather than 0-1
colormode(255)

# Set the pen color
pencolor(chartreuse)

# Move around
forward(100)
left(90)
forward(1000)

# Wait for input before closing
raw_input()
