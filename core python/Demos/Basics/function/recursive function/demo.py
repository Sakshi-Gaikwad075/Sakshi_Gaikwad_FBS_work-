def series(n):
    if (n > 0):
        print(n)
        series(n-1)
n = 5
series(n)

def val(n):
    count =0
    if(n>0):
        count += n
        series(n)
n = 5
series(n)