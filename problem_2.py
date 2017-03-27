first = 1
second = 2
third = first + second
result = second
while third <= 4000000:
    first = second
    second = third
    third = first + second
    if second % 2 == 0:
        result = result + second
print(result)