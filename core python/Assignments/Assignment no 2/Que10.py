# Reverse three digit number

n = int(input('Enter a number ='))

rev = 0

digit = n % 10
rev = rev * 10 + digit
n = n // 10

digit = n % 10
rev = rev * 10 + digit
n = n // 10

digit = n % 10
rev = rev * 10 + digit
print(rev)