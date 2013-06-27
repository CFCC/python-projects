#!/usr/bin/python

from turtle import*

colormode(255)

speed(0)

square_area=30

def colorsquare(input_color):
	pencolor(input_color)
	fillcolor(input_color)
	begin_fill()
	for i in range(4):
		forward(square_area)
		left(90)
	end_fill()

red1=[255,0,0]
red2=[114,0,0]
red3=[73,0,0]
red4=[54,0,0]
red5=[45,0,0]

row_foo=["white","white","white","white","white",red5,red5,"white","white","white","white","white"]

for colorme in row_foo:
	colorsquare(colorme)
	forward(square_area)

right(180)
forward(square_area*12)
left(90)
forward(square_area)
left(90)

row_goo=["white","white","white","white",red5,red2,red2,red5,"white","white","white","white"]

for colorme in row_goo:
	colorsquare(colorme)
	forward(square_area)

right(180)
forward(square_area*12)
left(90)
forward(square_area)
left(90)

row_hoo=["white","white","white",red5,red1,red2,red3,red3,red5,"white","white","white"]

for colorme in row_hoo:
	colorsquare(colorme)
	forward(square_area)

right(180)
forward(square_area*12)
left(90)
forward(square_area)
left(90)

row_joo=["white","white",red5,red2,red2,red2,red2,red3,red3,red5,"white","white"]

for colorme in row_joo:
	colorsquare(colorme)
	forward(square_area)

right(180)
forward(square_area*12)
left(90)
forward(square_area)
left(90)

row_koo=["white",red5,red2,red2,red2,red2,red2,red3,red4,red1,red5,"white"]

for colorme in row_koo:
	colorsquare(colorme)
	forward(square_area)

right(180)
forward(square_area*12)
left(90)
forward(square_area)
left(90)

row_loo=[red5,red1,red2,red2,red3,red2,red1,red3,red3,red3,red3,red5]

for colorme in row_loo:
	colorsquare(colorme)
	forward(square_area)

right(180)
forward(square_area*12)
left(90)
forward(square_area)
left(90)

row_moo=[red5,red2,red3,red2,red2,red2,red2,red3,red3,red4,red3,red5]

for colorme in row_moo:
	colorsquare(colorme)
	forward(square_area)

right(180)
forward(square_area*12)
left(90)
forward(square_area)
left(90)

row_noo=[red5,red3,red2,red1,red2,red2,red2,red3,red3,red3,red3,red5]

for colorme in row_noo:
	colorsquare(colorme)
	forward(square_area)

right(180)
forward(square_area*12)
left(90)
forward(square_area)
left(90)

row_poo=["white",red5,red3,red3,red2,red2,red4,red3,red3,red1,red5,"white"]

for colorme in row_poo:
	colorsquare(colorme)
	forward(square_area)

right(180)
forward(square_area*12)
left(90)
forward(square_area)
left(90)

row_roo=["white","white",red5,red5,red3,red3,red3,red3,red5,red5,"white","white"]

for colorme in row_roo:
	colorsquare(colorme)
	forward(square_area)

right(180)
forward(square_area*12)
left(90)
forward(square_area)
left(90)

row_soo=["white","white","white","white",red5,red5,red5,red5,"white","white","white","white"]

for colorme in row_soo:
	colorsquare(colorme)
	forward(square_area)

right(180)
forward(square_area*12)
left(90)
forward(square_area)
left(90)


raw_input()


