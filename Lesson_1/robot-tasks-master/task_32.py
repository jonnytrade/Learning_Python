#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_8_18():
    n=0
    while not wall_is_on_the_right():
        while wall_is_above() and wall_is_beneath():
            fill_cell()
            move_right()
        if wall_is_on_the_right():
            break
        while not wall_is_above():
            move_up()
            if cell_is_filled():
                n+=1
            fill_cell()
        while not wall_is_beneath():
            move_down()
        move_right()
    mov('ax',n)






if __name__ == '__main__':
    run_tasks()
