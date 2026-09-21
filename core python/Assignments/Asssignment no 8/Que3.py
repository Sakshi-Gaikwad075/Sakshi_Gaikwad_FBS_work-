# Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
# b. 1!+ 2! + 3! + 4!+..... + n!
# c. 1^1 + 2^2 + 3^3+ ...... n^n


# A. 
def sum_natural(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
print(sum_natural(4))


# B.
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def sum_factorial(n):
    total = 0
    for i in range(1, n + 1):
        total += factorial(i)
    return total
print(sum_factorial(4))


# C.
def sum_power(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** i
    return total
print(sum_power(4))