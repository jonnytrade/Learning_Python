import turtle
from time import sleep
turtle.shape('turtle')

def face():
    turtle.width(5)
    turtle.color("blue")
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()

def eyes():
    turtle.width(5)
    turtle.color("red")
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()
    turtle.pu()
    turtle.fd(100)
    turtle.pd()
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()


def smile():
    turtle.right(90)
    turtle.width(5)
    turtle.color("green")
    turtle.right(90)
    turtle.fd(30)
    turtle.pu()
    turtle.fd(10)
    #turtle.left(180)
    turtle.fd(5)
    turtle.right(90)
    turtle.fd(50)
    turtle.setheading(270)
    turtle.pd()
    turtle.color("yellow")
    turtle.circle(50,180)

turtle.speed(1)
for i in range(1):
    face()
    turtle.pu()
    turtle.fd(-50)
    turtle.left(90)
    turtle.fd(120)
    turtle.setheading(0)
    turtle.pd()
    eyes()
    turtle.pu()
    turtle.setpos(0,0)
    turtle.left(90)
    turtle.fd(120)
    turtle.pd()
    smile()
    done()





