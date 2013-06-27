#!/usr/bin/python

from turtle import *

colormode(255)

brown = [137, 87, 1]

pencolor("orange")

forward(200)

backward(400)

forward(400)

pencolor("yellow")

left(90)

forward(100)

left(90)

forward(400)

left(90)

forward(100)

pencolor(brown)

forward(100)

left(90)

forward(400)

left(90)

forward(100)

penup()

backward(100)

left(90)

forward(100)

pendown()

left(90)

pencolor("red")

forward(200)

right(90)

forward(200)

right(90)

forward(200)

penup()

forward(200)

pendown()

pencolor("black")

forward(100)

left(90)

forward(100)

left(90)

forward(100)

forward(400)

left(90)

forward(400)

left(90)

forward(500)

left(90)

forward(100)

left(90)

forward(100)

backward(100)

right(90)

forward(300)

left(90)

forward(100)

left(90)

def colorsquare(input_color):
	
	pencolor(input_color)
	
	fillcolor(input_color)

	begin_fill()

	for i in range (4):

		forward(100)

		left(90)

	end_fill()
	
colorsquare("black")

forward(100)

penup()

forward(200)

pendown()

colorsquare("black")

penup()

backward(300)

right(90)

forward(100)

left(90)

pendown()

colorsquare("yellow")

pencolor("orange")

forward(100)

colorsquare("yellow")

pencolor("orange")

forward(100)

colorsquare("yellow")

pencolor("orange")

forward(100)

colorsquare("yellow")

pencolor("orange")

forward(100)

backward(400)

right(90)

penup()

forward(100)

left(90)

pendown()

colorsquare(brown)

pencolor(brown)

forward(100)

colorsquare(brown)

pencolor(brown)

forward(100)

colorsquare(brown)

pencolor(brown)

forward(100)

colorsquare(brown)

pencolor(brown)

forward(100)

left(90)

pencolor("black")

forward(100)

left(90)

pencolor("orange")

forward(400)

left(90)

pencolor("black")

forward(100)

left(90)

pencolor(brown)

forward(100)

right(90)

pencolor("red")

forward(101)

left(90)

colorsquare("red")

pencolor("red")

forward(100)

colorsquare("red")

pencolor("red")

backward(100)

right(90)

forward(100)

left(90)

colorsquare("red")

pencolor("red")

forward(100)

colorsquare("red")

pencolor("red")

forward(100)

pencolor("black")

forward(100)

left(90)

forward(200)

left(90)

pencolor(brown)

forward(400)

pencolor("black")

right(90)

penup()

forward(100)

pendown()

forward(200)

right(90)

forward(400)

right(90)

forward(200)

raw_input()