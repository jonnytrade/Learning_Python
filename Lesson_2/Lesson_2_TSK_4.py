import turtle



turtle.shape('turtle')
n=10
m=-10
s=100
for i in range(11):
     turtle.left(90)
     turtle.forward(s)
     turtle.left(90)
     turtle.forward(s)
     turtle.left(90)
     turtle.forward(s)
     turtle.left(90)
     turtle.forward(s)
     turtle.penup()
     turtle.goto(n,m)
     turtle.pendown()
     n+=10
     m-=10
     s+=20



