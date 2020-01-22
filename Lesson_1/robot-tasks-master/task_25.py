#!/usr/bin/python3

from pyrob.api import *

def paint_krest():
    fill_cell()
    move_down(2)
    fill_cell()
    move_up()
    fill_cell()
    move_left()
    fill_cell()
    move_right(2)
    fill_cell()

def perehod():
    move_right(3)
    move_up()



@task
def task_2_2():
    move_right()
    move_down()
    while not wall_is_on_the_right():
        paint_krest()
        if not wall_is_on_the_right():
            perehod()
    move_left(2)
    move_up()



if __name__ == '__main__':
    run_tasks()
