# 1. pass : neglect expected indentation error

# for i in range(1,10):
#    pass
#    print(i)

# 2.break : for terminating loop 
# for i in range(1,10):
#     if(i==4):
#         break
#     print(i)






# 3. continue: to stop perticular iteration
# for i in range(1,10):
#     if(i==4):
#         continue
#     print(i)


# 4.else:Will execute when loop executed successfully
for i in range(1,10):
    if(i==4):
        break
    print(i)
else:
    print('Else block executed.')