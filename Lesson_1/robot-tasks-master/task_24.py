#!/usr/bin/python3

from pyrob.api import *

def paint_crest():
    move_up()
    fill_cell()
    move_down(2)
    fill_cell()
    move_up()
    fill_cell()
    move_right()
    fill_cell()
    move_left(2)
    fill_cell()

def ishodnaya_posicia():
    move_right(2)
    move_down(2)


@task
def task_2_1():
    ishodnaya_posicia()
    paint_crest()
    move_up()



if __name__ == '__main__':
    run_tasks()
