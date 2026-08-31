# input 5 sub marks and display grade
s1 = int(input('Enter subject 1 marks ='))
s2 = int(input('Enter subject 2 marks ='))
s3 = int(input('Enter subject 3 marks ='))
s4 = int(input('Enter subject 4 marks ='))
s5 = int(input('Enter subject 5 marks ='))

total = s1 + s2 + s3 + s4 + s5
percentage = total / 5
print('percentage =',percentage)

if percentage >= 75:
    print('First class')
elif percentage >= 60:
    print('Second class')
elif percentage >= 40:
    print('Pass class')
else:
    print("fail")