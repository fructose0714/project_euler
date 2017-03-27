import math

a = 9
first = True
while a != 0:
    b = 9
    while b != -1:
        c = 9
        while c != -1:
            n = a + b * 10 + c * 100 + c * 1000 + b * 10000 + a * 100000
            d = math.floor(math.sqrt(n))
            while d >= 100:
                if n % d == 0 and first:
                    if n / d < 1000:
                        print(n)
                        print(d)
                        print(n / d)
                        first = False
                d = d - 1
            c = c - 1
        b = b - 1
    a = a - 1

