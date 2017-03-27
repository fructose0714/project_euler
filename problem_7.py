pl = [2]
n = 3
while len(pl) != 10001:
    nIsPrime = True
    for p in pl:
        if n % p == 0:
            nIsPrime = False
            break
    if nIsPrime:
        pl.append(n)
    n = n + 1
print(pl[10000])