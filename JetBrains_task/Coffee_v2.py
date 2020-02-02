water = int(input('Write how many ml of water the coffee machine has:'))
milk = int(input('Write how many ml of milk the coffee machine has:'))
coffee = int(input('Write how many grams of coffee beans the coffee machine has:'))
cup = int(input('Write how many cups of coffee you will need:'))
total = 0
water_1 = 200
milk_1 = 50
coffee_1 = 15
bank_water = water // water_1
bank_milk = milk // milk_1
bank_coffee = coffee // coffee_1
c= min(bank_water, bank_milk, bank_coffee)
buffer = 0
if c != 0:
    buffer = cup - c
else:
    buffer = 0
if cup == c:
    print('Yes, I can make that amount of coffee')
if c > cup:
    print("Yes, I can make that amount of coffee (and even", buffer, "more than that")
if cup > c:
    print('No, I can make only', c, 'cups of coffee')
