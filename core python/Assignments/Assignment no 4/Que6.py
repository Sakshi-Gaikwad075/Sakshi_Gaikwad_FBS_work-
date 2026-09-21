# 6. WAP to check if a given number is prime number or not.
n = 45
count = 0
for i in range(2,n):
    if n % i == 0:
        count += 1
if count == 0:
    print('Number is prime')
else:
    print('Number is not prime')