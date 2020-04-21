from sys import exit as prog_exit

bank_water = 400
bank_milk = 540
bank_coffee = 120
bank_money = 550
bank_cups = 9

def bank_result():
    print("The coffee machine has:")
    print(bank_water, "of water")
    print(bank_milk, "of milk")
    print(bank_coffee, "of coffee beans")
    print(bank_cups, "of disposable cups")
    print("$", bank_money, " of money", sep='')
    print("")
    command_line()

def fill_func():
    global bank_water, bank_milk, bank_coffee, bank_cups
    water_add = int(input("Write how many ml of water do you want to add:\n> "))
    milk_add = int(input("Write how many ml of milk do you want to add:\n> "))
    coffee_add = int(input("Write how many grams of coffee beans do you want to add:\n> "))
    cups_add = int(input("Write how many disposable cups of coffee do you want to add:\n> "))
    bank_water += water_add
    bank_milk += milk_add
    bank_coffee += coffee_add
    bank_cups += cups_add
    print("")
    command_line()

def take_func():
    global bank_money
    print("I gave you $", bank_money, sep='')
    print("")
    bank_money = 0
    command_line()

def coffee_made():
    global bank_water, bank_milk, bank_coffee, bank_cups, bank_money
    type_coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: >")
    if type_coffee == "1":
        if bank_water < 250:
            print("Sorry, not enough water!")
        else:
            if bank_coffee < 16:
                print("Sorry, not enough coffee!")
            else:
                if bank_cups < 1:
                    print("Sorry, not enough cups!")
                else:
                    bank_water -= 250
                    bank_coffee -= 16
                    bank_cups -= 1
                    bank_money += 4
                    print("I have enough resources, making you a coffee!")
    elif type_coffee == "2":
        if bank_water < 350:
            print("Sorry, not enough water!")
        else:
            if bank_coffee < 20:
                print("Sorry, not enough coffee!")
            else:
                if bank_milk < 75:
                    print("Sorry, not enough milk!")
                else:
                    if bank_cups < 1:
                        print("Sorry, not enough cups!")
                    else:
                        bank_water -= 350
                        bank_coffee -= 20
                        bank_milk -= 75
                        bank_cups -= 1
                        bank_money += 7
                        print("I have enough resources, making you a coffee!")
    elif type_coffee == "3":
        if bank_water < 200:
            print("Sorry, not enough water!")
        else:
            if bank_coffee < 12:
                print("Sorry, not enough coffee!")
            else:
                if bank_milk < 100:
                    print("Sorry, not enough milk!")
                else:
                    if bank_cups < 1:
                        print("Sorry, not enough cups!")
                    else:
                        bank_water -= 200
                        bank_coffee -= 12
                        bank_milk -= 100
                        bank_cups -= 1
                        bank_money += 6
                        print("I have enough resources, making you a coffee!")
    elif type_coffee == "back":
        command_line()
    command_line()


def command_line():
    action = input("Write action (buy, fill, take, remaining, exit):\n> ")
    if action == " remaining":
        print("")
        bank_result()
    elif action == "fill":
        fill_func()
    elif action == "take":
        take_func()
    elif action == "buy":
        coffee_made()
    elif action == "exit":
        prog_exit()


bank_result()
command_line()
