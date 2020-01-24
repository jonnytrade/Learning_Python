def fibo(n):
    first = 0
    second = 1

    if n < 1:
        return -1

    if n == 1:
        print(first)
        return first

    if n == 2:
        print(second)
        return second

    count = 3
    while count <= n:
        fib_n = first + second
        first = second
        second = fib_n
        count += 1
    print(fib_n)
    return fib_n

fibo(9)



