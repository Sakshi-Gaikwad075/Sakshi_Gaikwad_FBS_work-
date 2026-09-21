# without passing parameter with returning value

def strong():
    n = int(input('Enter number :'))
    temp = n
    sum = 0
    while n > 0:
        r = n % 10
        fact = 1

        for i in range(1,r+1):
            fact = fact * i
        sum = sum + fact
        n = n // 10

    if temp == sum:
        return(True)
    else:
        return(False)
print(strong())