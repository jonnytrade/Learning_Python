#!/usr/bin/python3

from pyrob.api import *

def test_wall():
    move_right()
    if wall_is_on_the_right():
        return True
    else:
        move_left()
        return False


@task
def task_7_5():
    move_right()
    fill_cell()
    m=1
    n=0
    while not wall_is_on_the_right():
        for i in range(m):
            if not wall_is_on_the_right():
                move_right()
                n+=1
                if n==m:
                    fill_cell()
                    n=0
        m+=1




if __name__ == '__main__':
    run_tasks()
