# 5. WAP to print Fibonacci series upto n.

n = int(input('Enter a number ='))
a = 0
b = 1
for i in range(n):
    c = a+b

    print(c)
    a = b 
    b = c    
    
    