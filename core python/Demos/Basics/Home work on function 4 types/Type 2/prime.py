# with passing parameter without returning value

def prime(n):
    count = 0

    for i in range(2,n):
        if(n % i == 0):
           count += 1
    if count == 0:
        print(True)
    else:
        print(False)
n = int(input('Enter number :'))
prime(n)