"""Задание:
Написать программу которая проверяет попало ли целое число в интервал от 50 до 100 и сообщить результат на экран
в следующем виде: "Число a не содержится в интервале" или "Число a содержится в интервале". Где a это переменная."""

a=int(input())

if a > 50 and a < 100:
    print("Число", a, "содержиться в интервале от 50 до 10")
else:
    print("Число", a, "не содержиться в интервале от 50 до 100")
