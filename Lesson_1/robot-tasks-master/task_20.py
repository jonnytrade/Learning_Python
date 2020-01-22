#!/usr/bin/python3

from pyrob.api import *


def test_right_side():
    move_right(2)
    if wall_is_on_the_right():
        move_left()
        fill_cell()
        move_down()
        fill_cell()
        return False
    else:
        move_left(2)
        return True


def test_left_side():
    move_left(2)
    if wall_is_on_the_left():
        move_right()
        fill_cell()
        move_down()
        return False
    else:
        move_right(2)
        return True


def test_bottom():
    move_down()
    if wall_is_beneath():
        move_up()
        return False
    else:
        move_up()
        return True


@task(delay=0.05)
def task_4_3():
    move_right()
    while test_bottom():
        while test_right_side():
            fill_cell()
            move_right()
            fill_cell()
        while test_left_side():
            move_left()
            fill_cell()


if __name__ == '__main__':
    run_tasks()
