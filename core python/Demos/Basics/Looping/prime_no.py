# n = int(input('enter number:'))
# for i in range(2,n):
#     if(n%i ==0):
#         print(f'{n}not prime number')
#         break
# else:
#     print(f'{n}prime number')




# for n in range(2,101):
#     count = 0
#     for i in range(1,n+1):

#         if(n%i == 0):
#             count +=1
#     if count == 2:
#         print(n)





n = int(input('enter number:'))
for n in range(2,n+1):
    for i in range(2,n):
        if(n%i ==0):
            
            break
    else:
        print(n, end=' ')
