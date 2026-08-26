# check no is +ve or -ve or neutral
n = int(input('Enter a number:'))
if(n>0):
    print(f'{n} is positive number.')
elif(n==0):
    print(f'{n} is neutral number.')
else:
    print(f'{n} is negative number.')
    