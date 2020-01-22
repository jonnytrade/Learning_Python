#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_10():
    while not wall_is_on_the_right():
        if wall_is_above() and not wall_is_beneath():
            move_down()
            fill_cell()
            move_up()
        else:
            if wall_is_beneath() and not wall_is_above():
                move_up()
                fill_cell()
                move_down()
            else:
                if not wall_is_beneath() and not wall_is_above():
                    move_up()
                    fill_cell()
                    move_down(2)
                    fill_cell()
                    move_up()
        move_right()
    if wall_is_above() == False and wall_is_beneath() == False:
        move_up()
        fill_cell()
        move_down(2)
        fill_cell()
        move_up()
    else:
        if wall_is_beneath() == True and wall_is_above() == False:
            move_up()
            fill_cell()
            move_down()
        else:
            if wall_is_above() == True and wall_is_beneath() == False:
                move_down()
                fill_cell()
                move_up()








if __name__ == '__main__':
    run_tasks()
