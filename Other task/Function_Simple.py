from math import sqrt

n = int(input())


def simple(n):
    if n < 2:
        print("This number is not prime")
        quit()
    if n == 2:
        print("This number is prime")
        quit()
    limit = sqrt(n)
    i = 2
    while i <= limit:
        if n % i == 0:
            print("This number is not prime")
            quit()
        i += 1
    print("This number is prime")


simple(n)