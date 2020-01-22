#!/usr/bin/python3

from pyrob.api import *

def test_corner():
    if wall_is_on_the_left() and wall_is_beneath():
        return True
    else:
        return False



@task(delay=0.2)
def task_9_3():
    x=0  # Начало поля
    s=0  # Длинна поля
    m=0  # Текущий шаг
    y=0  # Конец поля
    "y=s"  # Не тут))
    while not wall_is_on_the_right():  # Длинна поля
        move_right()
        s+=1
    y=s  # Вот сюда нужно)
    while not wall_is_on_the_left():
        move_left()
    for i in range(s):
        while not wall_is_on_the_right():
            'm=1' # Не нужно!!
            if m!=x and m!=y:  # Заменил 1 на x.
                'move_right()'  # Тут не нужно
                fill_cell()
            move_right()
            m+=1
        if m!=y: # Этот IF нужен что бы проверять последнею клетку в ряду.
            fill_cell()
        'm+=1' # m это текущий щаг. Он должен быть в цикле
        x+=1
        y-=1
        move_down()
        while not wall_is_on_the_left():
            move_left()
        m=0 # Обнуляем текущий шаг


if __name__ == '__main__':
    run_tasks()
