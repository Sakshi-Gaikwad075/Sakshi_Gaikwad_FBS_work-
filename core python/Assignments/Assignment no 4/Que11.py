# WAP to check strong number
n = 145
sum = 0
temp = n
while n > 0:
    r = n % 10
    fact = 1
    for i in range(1,r+1):
        fact = fact * i
    sum = sum + fact
    n = n // 10
if temp == sum:
    print('Strong number')
else:
    print('Not strong number')