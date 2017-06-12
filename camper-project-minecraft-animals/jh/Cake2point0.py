from turtle import *
def box(hashtagyoloswag):
    pencolor(hashtagyoloswag)
    begin_fill()
    fillcolor(hashtagyoloswag)
    for i in range(4):    
            forward(50)
            left(90)
    end_fill()

def newrow():
    left(180)
    penup()
    forward(800)
    left(90)
    forward(50)
    left(90)

speed(0)
ht()
gray = [194, 194, 194]
grayer = [188, 188, 188]
grayish = [206, 206, 206]
grayest = [73, 73, 73]
white = [234, 233, 235]
purewhite = [255, 255, 255]
brown1 = [164, 69, 0]
brown2 = [181, 79, 0]
brown3 = [199, 89, 8]
brown4 = [189, 84, 2]
brown5 = [66, 28, 5]
red = [255, 0, 0]
colormode(255)

row1 = [purewhite, purewhite, purewhite, purewhite, purewhite, grayest, grayest, grayest, grayest, grayest, grayest, purewhite, purewhite, purewhite, purewhite, purewhite]
row2 = [purewhite, purewhite, purewhite, grayest, grayest, gray, gray, gray, gray, gray, gray, grayest, grayest, purewhite, purewhite, purewhite]
row3 = [purewhite, grayest, grayest, gray, gray, white, red, white, white, white, white, gray, gray, grayest, grayest, purewhite]
row4 = [grayest, gray, gray, red, white, white, white, white, white, white, red, white, white, gray, gray, grayest]
row5 = [grayest, gray, white, white, white, white, white, white, red, white, white, white, red, white, gray, grayest]
row6 = [grayest, gray, gray, white, red, white, white, white, white, white, white, white, white, gray, gray, grayest]
row7 = [grayest, grayish, white, gray, gray, white, white, white, red, white, white, gray, gray, grayer, grayer, grayest]
row8 = [brown5, grayish, white, white, white, gray, gray, gray, gray, gray, gray, grayer, grayer, grayer, grayer, brown5]
row9 = [brown5, brown1, grayish, white, white, white, grayish, grayish, grayish, grayer, grayer, grayer, grayer, brown2, brown1, brown5]
row10 = [brown5, brown1, brown2, brown2, white, grayish, grayish, grayish, grayish, grayer, grayer, grayer, brown2, brown2, brown1, brown5]
row11 = [brown5, brown1, brown3, brown3, brown4, brown2, gray, brown2, brown2, brown2, grayer, brown4, brown2, brown2, brown1, brown5]
row12 = [purewhite, brown5, brown5, brown1, brown1, brown3, brown3, brown4, brown4, brown4, brown4, brown1, brown1, brown1, brown5, purewhite]
row13 = [purewhite, purewhite, purewhite, brown5, brown5, brown1, brown1, brown1, brown1, brown1, brown1, brown5, brown5, brown5, purewhite, purewhite]
row14 = [purewhite, purewhite, purewhite, purewhite, purewhite, brown5, brown5, brown5, brown5, brown5, brown5, purewhite, purewhite, purewhite, purewhite, purewhite]
rows = [row1, row2, row3, row4, row5, row6, row7, row8, row9, row10, row11, row12, row13, row14]

penup()
goto(-400, 300)
pendown()
for row in rows:
    for color in row:
        box(color)
        forward(50)
    newrow()


raw_input()