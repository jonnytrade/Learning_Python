def balance(brackets):
    check = 0
    for n in brackets:
        if n == "[":
            check += 1
        else:
            check -= 1
    if check == 0:
        print ("True")
    else:
        print ("False")

balance("[][[")

