n = 600851475143
q = 2
while n != 1:
    while n % q == 0:
        n = n / q
    q = q + 1
print(q - 1)