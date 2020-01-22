#!/usr/bin/python3

from pyrob.api import *

def paint_krest_right():
    move_down(2)
    fill_cell()
    move_up()
    move_left()
    fill_cell()
    move_right()
    fill_cell()
    move_right()
    fill_cell()

def paint_krest_left():
    move_down(2)
    fill_cell()
    move_up()
    move_right()
    fill_cell()
    move_left()
    fill_cell()
    move_left()
    fill_cell()

def test_corner():
    move_down()
    if wall_is_on_the_left() and wall_is_beneath():
        return False
    else:
        return True

def perehod_r_l():
    move_right(3)
    move_up()

def perehod_l_r():
    move_left(3)
    move_up()

def perehod_down_1():
    move_down(3)
    move_left()

def perehod_down_2():
    move_down(3)
    move_right()



@task(delay=0.02)
def task_2_4():
    move_right()
    move_up()
    while test_corner():
        while not wall_is_on_the_right():
            paint_krest_left()
            perehod_r_l()




if __name__ == '__main__':
    run_tasks()
