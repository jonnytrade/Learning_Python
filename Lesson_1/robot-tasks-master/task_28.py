#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    n=0
    while not wall_is_on_the_right():
        if cell_is_filled():
            move_right()
            n+=1
            if n==5:
                move_left()
                break
        else:
            move_right()




if __name__ == '__main__':
    run_tasks()
