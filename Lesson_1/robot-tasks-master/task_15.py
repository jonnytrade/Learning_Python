#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    if wall_is_above() and wall_is_on_the_left():
      while not wall_is_beneath():
          move_down()
      while not wall_is_on_the_right():
          move_right()
    elif wall_is_above() and wall_is_on_the_right():
            while not wall_is_beneath():
                  move_down()
            while not wall_is_on_the_left():
                  move_left()
    elif wall_is_on_the_left() == True and wall_is_beneath() == True:
                while wall_is_on_the_right() == False:
                      move_right()
                while wall_is_above() == False:
                      move_up()
    elif wall_is_beneath() == True and wall_is_on_the_right() == True:
                    while wall_is_on_the_left() == False:
                        move_left()
                    while wall_is_above()== False:
                        move_up()







if __name__ == '__main__':
    run_tasks()
