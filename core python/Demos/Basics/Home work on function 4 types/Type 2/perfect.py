# with passing parameter without returning value

def perfect(n):
    
    sum = 0

    for i in range(1,n):
        if n % i == 0:
            sum = sum + i

    if sum == n:
        print(True)
    else:
        print(False)

n = int(input('Enter number :'))
perfect(n)