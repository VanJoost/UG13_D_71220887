
import turtle
# Turtle object
pen = turtle.Turtle()

# function for creation of eye
def eye(col, rad):
    pen.down()
    pen.fillcolor(col)
    pen.begin_fill()
    pen.circle(rad)
    pen.end_fill()
    pen.up()

# draw face
pen.fillcolor('yellow')
pen.begin_fill()
pen.circle(100)
pen.end_fill()
pen.up()

# draw eye
pen.goto(-40, 120)
eye('white', 15)
pen.goto(-37, 125)
eye('black', 5)
pen.goto(40, 120)
eye('white', 15)
pen.goto(40, 125)
eye('black', 5)

# draw nose
# pen.goto(0, 75)
# eye('black', 8)

# draw mouth
pen.goto(-40, 85)
pen.down()
pen.right(90)
pen.circle(40, 180)
pen.up()
pen.end_fill()
pen.hideturtle()
sc = turtle.Screen().exitonclick()

# draw tongue
n.right(180)
pen.fillcolor('brown')
pen.begin_fill()
pen.circle(10, 180)
pen.end_fill()
pen.hideturtle()

import turtle
def drawPersegi(xPos, yPos, lebar):
     pen.up()
     pen.goto(xPos, yPos)
     pen.down()
     #perulangan untuk menggambar garis
     for i in range(4):
         pen.forward(lebar)
         pen.left(90)

drawPersegi(0, 0, 100)
drawPersegi(-300, -100, 200)
sc = turtle.Screen().exitonclick()