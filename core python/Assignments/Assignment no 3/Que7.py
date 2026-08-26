# write program to check if user has entered correct userid and pass
userid = input('Enter user ID:')
pass = input('Enter pass:')

if(userid == "admin" and pass == "1234"):
    print('Login Successful.')
else:
    print('Invalid user ID and Password.')