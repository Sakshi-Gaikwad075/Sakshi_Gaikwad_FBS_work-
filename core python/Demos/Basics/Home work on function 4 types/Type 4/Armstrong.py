# with passing parameter with returning value

def armstrong(n):
    
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
n = int(input('Enter number :'))
print(armstrong(n))