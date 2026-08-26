# take userid and pass after verifying userid and pass display 4 digit random no. and ask user to enter same. if user enter same no. 
# then show him success msg otherwise failed(something like captcha)

import random
userID =input('Enter user id =')
password = input('Enter password =')
if(userID =='1234' and password=='1234'):
    systemcaptcha = random.randrange(1000, 10000)
    print(systemcaptcha)
    captcha = int(input('Enter a captcha='))
    if( captcha == systemcaptcha):
        print('successfully log in')
    else:
        print('Invalid captcha')
else:
    print('Invalid ID and password')