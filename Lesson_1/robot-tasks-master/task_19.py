#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
    if not wall_is_on_the_right() and not wall_is_on_the_left():
        while wall_is_on_the_left() == False:
            move_left()
        if wall_is_on_the_left()  and wall_is_above():
           while not wall_is_on_the_right():
               move_right()
        else:
            while not wall_is_above():
                move_up()
        if wall_is_on_the_right() and not wall_is_above():
            while wall_is_above() == False:
                move_up()
            while wall_is_on_the_left() == False:
                move_left()

if __name__ == '__main__':
    run_tasks()
