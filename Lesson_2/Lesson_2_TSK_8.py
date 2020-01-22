import turtle
import math

turtle.shape('turtle')
n=3
r=20
turtle.pu()
turtle.left(135)
turtle.pd()
for i in range(9):
    f_angle=360/n
    f_rad=f_angle*math.pi/180
    a=2*r*math.sin(f_rad/2)
    turtle.pu()
    turtle.setpos(0,0)
    turtle.setheading(0)
    turtle.forward(r)
    turtle.left(90-f_angle/2)
    turtle.pd()
    for i in range(n):
        turtle.left(f_angle)
        turtle.forward(a)
    r+=20
    n+=1







