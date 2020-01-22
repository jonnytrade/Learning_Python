from graph import *
from tkinter import *
def fon():
    penColor(0,255,255)
    brushColor(0,255,255)
    rectangle(0, 0, 1000, 250)
    penColor(0,0,255)
    brushColor(0,0,255)
    rectangle(0, 250, 1000, 400)
    penColor(255, 255, 0)
    brushColor(255, 255, 0)
    rectangle(0, 400, 1000, 600)

def sky():
    penColor("yellow")
    brushColor("yellow")
    circle(850,80,50)
    penSize(1)
    penColor("black")
    brushColor("white")
    circle(100, 80, 20)
    circle(120, 70, 20)
    circle(120, 93, 20)
    circle(142, 70, 20)
    circle(165, 80, 20)
    circle(145, 95, 20)

def zont():
    penColor("red")
    brushColor("red")
    rectangle(180,320,190,550)
    polygon([(180, 320), (80, 370), (290, 370), (190, 320)])
    penColor("grey")
    line(180, 320, 110, 370)
    line(180, 320, 140, 370)
    line(180, 320, 170, 370)
    line(190, 320, 200, 370)
    line(190, 320, 230, 370)
    line(190, 320, 260, 370)

def korablik():
    penSize(2)
    penColor("black")
    brushColor("brown")
    arc(500, 320, 50, 50, 180, 90)
    line(450,320,500,320)
    polygon([(500, 320), (900, 320), (800, 370), (500, 370)]) # Корпус
    brushColor("black")
    rectangle(600,320,605,125) # Мачта
    penSize(1)
    brushColor("grey")
    polygon([(605, 125), (705, 222), 625, 222)]) # Парус
    polygon([(605, 320), (705, 222), (625, 222)]) # Парус
    penSize(2)
    penColor("black")
    brushColor("white")
    circle(820,340,12)
    line(800,320,800,370)




mainWindow()
windowSize(1000,600)
canvasSize(1000,600)
fon()
sky()
zont()
korablik()









#polygon([(0,0), (0,250), (1000,250), (1000,0)])

run()