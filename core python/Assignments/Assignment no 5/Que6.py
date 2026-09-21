n = int(input('Enter number'))
count = 0
num = 2
while count < n:
    c = 0
    for i in range(2,n):
        if (n % i == 0):
            c += 1

    if c == 2:
        print(num)
        count +=1
    num += num