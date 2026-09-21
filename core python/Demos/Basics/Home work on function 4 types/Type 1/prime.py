# without passing parameter without returning value

def prime():
    n = int(input('Enter number :'))
    count = 0

    for i in range(2,n):
        if(n % i == 0):
           count += 1
    if count == 0:
        print(True)
    else:
        print(False)
prime()