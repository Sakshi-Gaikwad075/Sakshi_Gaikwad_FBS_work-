id = 'sakshi'
passw = 123
for i in range(3):
    user_id = input('Enter user id =')
    password = int(input('Enter password ='))
    if (user_id == id and password == passw):
        print('successfully login.')
    else:
        print('Try again..')