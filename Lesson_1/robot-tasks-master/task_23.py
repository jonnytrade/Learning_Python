#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.1)
def task_6_6():
    move_right()
    m=1
    while not wall_is_on_the_right():
        for i in range(m):
             while wall_is_above() and not wall_is_on_the_right():
                move_right()
                m+=1
        while not wall_is_above():
                move_up()
                fill_cell()
        while not wall_is_beneath():
                fill_cell()
                move_down()
        if not wall_is_on_the_right():
                  move_right()
                  m+=1
    while not wall_is_above():
        move_up()
        fill_cell()
    while not wall_is_beneath():
        move_down()
    move_left(m)





if __name__ == '__main__':
    run_tasks()
