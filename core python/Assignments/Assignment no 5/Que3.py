n = int(input('Enter number of passenger ='))
cost = int(input('Enter cost of ticket ='))
total = 0
for i in range(1,n+1):
    age = int(input('Enter age='))

    if (age < 12):
        amount = cost * 0.70
    elif(age > 59):
        amount = cost * 0.50
    else:
        amount = cost

    total = total + amount

print(amount)
    