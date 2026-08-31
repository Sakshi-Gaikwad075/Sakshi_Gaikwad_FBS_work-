# check person is sligible for marriage
gender = input('Enter Gender =')
age = int(input('Enter age='))

if gender.lower() == 'male' and age >=21:
    print('Male is eligible for marriage')
elif gender.lower() =='female' and age >= 18:
    print('female is eligible for marriage')
else:
    print('not eligible')