import turtle

turtle.shape('turtle')

def flower():
    turtle.circle(50)
    #turtle.right(180)
    turtle.circle(-50)

for i in range (3):
    flower()
    turtle.right(45)



