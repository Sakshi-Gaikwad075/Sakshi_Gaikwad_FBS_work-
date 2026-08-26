# to check triangle is equilaterial, isosceles or scalene triangle

s1 = int(input('Enter 1st side:'))
s2 = int(input('Enter 2nd side:'))
s3 = int(input('Enter 3rd side:'))

if(s1==s2==s3):
    print('Equilaterial Triangle.')
elif(s1==s2 or s2==s3 or s1==s3):
    print('Isosceles Triangle')
else:
    print('Scalene triangle')