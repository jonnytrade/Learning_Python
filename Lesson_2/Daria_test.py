    x=1 #Начало поля
    s=0 #Длинна поля
    m=1 # Текущий шаг
    y=0 #Конец поля
    "y=s" # Не тут))
    while not wall_is_on_the_right(): #Длинна поля
        move_right()
        s+=1
    y=s # Вот сюда нужно)
    while not wall_is_on_the_left():
        move_left()
    while not wall_is_on_the_right():
        move_right() # Тут нужно
        "m=1 # Не нужно!!
        if m!=x or m!=y: # Заменил 1 на x.
            "move_right()" # Тут не нужно
            fill_cell()
        m+=1 # Вынес за цикл IF
        x+=1 # Вынес за цикл IF
        y-=1 # Вынес за цикл IF
        else:
            move_right()
            "m+=1" # Не нужно!!
    move_down(1)
    while not wall_is_on_the_left():
        move_left()
    while not wall_is_on_the_right():
        m=1
        if m!=x or m!=y:
            move_right()
            fill_cell()
            m+=1
            x+=1
            y-=1
        else:
            move_right()
            m+=1