a = input()
b = input()
c = input()

if a > b and b > c:
    print(a)
if a > c and c > b:
    print(a)
if b > a and a > c:
    print(b)
if b > c and c > b:
    print(b)
if c > a and a > b:
    print(c)
if c > b and b > a:
    print(c)
if c == a:
    print(a or c)
if b == c:
    print(b or c)
if c == a and b == a:
    print(c or a or b)
