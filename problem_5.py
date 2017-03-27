def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

i = 20
result = 1
while i != 1:
    result = result * (i / gcd(i, result))
    i = i - 1
print(result)