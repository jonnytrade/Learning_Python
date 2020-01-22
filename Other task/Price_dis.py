price = int(input())
if price >= 300:
    price *=0.75
elif price >= 200 and price < 300:
    price *= 0.8
elif price >= 100 and price < 200:
    price *=0.9
else:
    price *= 0.95

print(price)

