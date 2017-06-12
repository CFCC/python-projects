#!/usr/bin/python

from turtle import *

colormode(255)

def colorsquare(input_color):

	pencolor(input_color)
	
	fillcolor(input_color)

	begin_fill()

	for i in range (4):

		forward(50)

		left(90)

	end_fill()

squarelength = (50)

crust = [231, 156, 95]

middle_top = [222, 134, 82]

some_corners_right = [196, 87, 34]

nextocorn_right = [210, 97, 40]

nextocorn_left = [210, 108, 56]

undmid = [216, 119, 70]

other_corn = [196, 97, 46]

spots = [207, 113, 63]

light_crust = [251, 202, 125]

spots_two = [223, 127, 80]

undmidark = [216, 105, 50]

darkb = [141, 97, 25]

darkercru = [191, 139, 59]

outcru = [210, 157, 74]

cut_slice = [234, 145, 101]

nexcutslice = [207, 100, 44]

oth_corn_oo = some_corners_right

ligdakcru = [231, 179, 98]

nexct = [201, 89, 34]

undct = [184, 76, 23]

low_smi_d_crust = [231, 179, 98]

speed(0)

penup()

backward(400)

left(90)

forward(250)

right(90)

pendown()

row_a = ["white","white","white","white",crust,crust,middle_top,middle_top,crust,crust,"white","white","white","white"]

row_b = ["white", "white",crust,crust,some_corners_right,nextocorn_right,undmid,undmid,nextocorn_left,some_corners_right,crust,crust,"white","white"]

row_c = ["white",crust,other_corn,nextocorn_left,undmid,undmid,undmid,spots,undmid,undmid,nextocorn_left,some_corners_right,crust,"white"]

row_d = [crust,some_corners_right,nextocorn_left,undmid,spots,undmid,spots_two,undmidark,undmid,undmid,undmid,nextocorn_left,some_corners_right,crust]

row_e = [light_crust,some_corners_right,nextocorn_left,cut_slice,cut_slice,cut_slice,cut_slice,cut_slice,nexcutslice,undmidark,undmidark,nextocorn_left,oth_corn_oo,light_crust]

row_f = [ligdakcru,crust,cut_slice,nexct,nexct,undct,undct,cut_slice,undmid,undmid,nextocorn_left,oth_corn_oo,crust,ligdakcru]

row_g = [ligdakcru,nexct,nexct,nexct,undct,undct,cut_slice,nextocorn_left,nextocorn_left,some_corners_right,crust,light_crust,ligdakcru,outcru]

row_h = [darkercru,nexct,nexct,undct,darkb,darkb,cut_slice,light_crust,light_crust,light_crust,low_smi_d_crust,low_smi_d_crust,darkercru,darkb]

row_i = ["white",darkercru,darkercru,darkb,"white","white",ligdakcru,ligdakcru,ligdakcru,ligdakcru,outcru,darkercru,darkb,"white"]

row_j = ["white","white","white","white","white","white",ligdakcru,ligdakcru,outcru,darkercru,darkb,darkb,"white","white"]

row_k = ["white","white","white","white","white","white",darkb,darkb,darkb,darkb,"white","white","white","white"]

def goback():

	backward(700)

	right(90)

	forward(50)

	left(90)

rows = [row_a,row_b,row_c,row_d,row_e,row_f,row_g,row_h,row_i,row_j,row_k]

for row in rows:
	for color in row:
		colorsquare(color)
		forward(squarelength)
	goback()

raw_input("l")