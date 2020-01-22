#!/usr/bin/python3

from pyrob.api import *

def test_bottom():
    move_down()
    if wall_is_beneath():
        move_up()
        return False
    else:
        move_up()
        return True


@task(delay=0.05)
def task_4_11():
    m=2
    move_right()
    move_down()
    fill_cell()
    while test_bottom():
        move_down()
        while not wall_is_on_the_left():
            move_left()
        for i in range(m):
            move_right()
            fill_cell()
        m+=1
    move_left(m-2)
    move_down()








if __name__ == '__main__':
    run_tasks()
