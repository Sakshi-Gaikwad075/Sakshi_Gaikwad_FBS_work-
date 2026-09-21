# without passing parameter without returning value

def armstrong():
    n = int(input('Enter number :'))
    temp = n
    sum = 0

    while n > 0:
        r = n % 10
        sum = sum + r * r * r
        n = n // 10

    if temp == sum:
        print(True)
    else:
        print(False)
armstrong()