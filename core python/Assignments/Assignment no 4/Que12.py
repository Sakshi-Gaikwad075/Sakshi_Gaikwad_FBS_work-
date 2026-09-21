# to check number is armstrong or not
n = 153
temp = n
sum = 0
while n > 0:
    r = n % 10
    sum = sum + r * r * r
    n = n // 10
if sum == temp:
    print('number is armstrong')
else:
    print('Number is not armstrong.')