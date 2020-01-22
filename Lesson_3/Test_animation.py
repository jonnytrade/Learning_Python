from graph import *

def update():
    moveObjectBy(obj,5,0)
    if xCoord(obj)>= 490:
        close()
onTimer(update,50)

brushColor("red")
rectangle(0,0,500,500)

brushColor("yellow")
obj=rectangle(100,100,120,120)
update()
run()
