# without passing parameter with returning value

def armstrong():
    n = int(input('Enter number :'))
    temp = n
    sum = 0

    while n > 0:
        r = n % 10
        sum = sum + r * r * r
        n = n // 10

    if temp == sum:
        return(True)
    else:
        return(False)
print(armstrong())