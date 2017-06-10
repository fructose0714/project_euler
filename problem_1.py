result = 0
for n in range(1000):
    if n % 5 == 0 or n % 3 == 0:
        result = result + n
print(result)