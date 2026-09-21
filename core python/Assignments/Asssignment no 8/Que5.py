# Sum of all prime numbers between 1 to n

def prime(n):
    count = 0
    for i in range(1,n):
        if n % i == 0:
            count += 1
    return count
n = int(input('Enter number:'))
print(prime(n))