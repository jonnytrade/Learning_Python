#!/usr/bin/python3

from pyrob.api import *

def left_corner():
    if wall_is_on_the_left() and wall_is_beneath():
        return False
    else:
        return True

@task
def task_5_10():
    while left_corner():
        while not wall_is_on_the_right():
            fill_cell()
            move_right()
            fill_cell()
        move_down()
        while not wall_is_on_the_left():
            fill_cell()
            move_left()
    fill_cell()



if __name__ == '__main__':
    run_tasks()
