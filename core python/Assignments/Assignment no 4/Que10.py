# WAP to check if given number is perfect number
n = 6
sum = 0
for i in range(1,n):
    if n % i == 0:
        sum = sum + i
if n == sum:
    print('Perfect number.')
else:
    print('not perfect number.')