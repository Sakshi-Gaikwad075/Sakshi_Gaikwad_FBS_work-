# take input angles of triangle and check triangle is valid or not

a1 = int(input('Enter 1st angle:'))
a2 = int(input('Enter 2nd angle:'))
a3 = int(input('Enter 3rd angle:'))
sum = a1+a2+a3
if(sum == 180):
    print('Triangle is valid')
else:
    print('Triangle is Not Valid')

    