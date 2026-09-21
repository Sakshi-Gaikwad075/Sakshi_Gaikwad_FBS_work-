# with passing parameter without returning value

def armstrong(n):
    
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
n = int(input('Enter number :'))
armstrong(n)