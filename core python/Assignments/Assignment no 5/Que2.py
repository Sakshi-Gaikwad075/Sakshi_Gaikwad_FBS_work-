n = int(input('Enter number = '))
sum = 0
for i in range(1,n+1):
    total = 0
    for j in range(1,6):
        marks = int(input('Enter marks ='))
        total = total + marks
    percentage = total / 5
    print(f'student {i} percentage = {percentage}')

    sum = sum + percentage
average = sum / n

print('Average Percentage =', average)

        