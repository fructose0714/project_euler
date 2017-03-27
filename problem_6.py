import math

def sum(n):
    if n == 1: return 1
    return sum(n - 1) + n

def sumOfSquare(n):
    if n == 1: return 1
    return sumOfSquare(n - 1) + pow(n, 2)

print(pow(sum(100), 2) - sumOfSquare(100))