"""Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.

Найдите сумму всех чисел меньше 1000, кратных 3 или 5."""

n = 0
i = 0
while n < 1000:
    if n % 3 == 0 or n % 5 == 0:
        i = i + n
        n += 1
    else:
        n += 1
print(i)