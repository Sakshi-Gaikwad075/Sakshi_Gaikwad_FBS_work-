# 1. to pass multiple para to function
# 2. mention astrisk(*) symbol before para in functin defination
# 3. value store in tuple



def addition(*num):
    sum = 0
    for val in num:
        sum += val
    return sum
res = addition(10,20,30,40,50)
print(res)

