#!/usr/bin/python3

from pyrob.api import *
def test_bottom():
    if wall_is_on_the_left() and wall_is_beneath():
        return True
    else:
        return False
def start():
    n=0
    while n<2:
        while not wall_is_on_the_left():
            move_left()
            if not wall_is_beneath():
                move_down()
                n=0
        n+=1
        while not wall_is_on_the_right():
            move_right()
            if not wall_is_beneath():
                move_down()
                n=0
        n+=1
    else:
        while not wall_is_on_the_left():
            move_left()


@task(delay=0.1)
def task_8_30():
        start()




if __name__ == '__main__':
    run_tasks()
