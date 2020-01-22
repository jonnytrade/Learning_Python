def factorial(n):
    l = n
    while (n-l)!=1:
        n=n*(n-l)
        l-=1
    print(n)
factorial(10)
