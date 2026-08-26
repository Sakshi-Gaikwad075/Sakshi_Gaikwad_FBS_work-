# W . P. to accept integer amt from user and tell min number of notes needed for representing amt
amt = int(input('Enter amount ='))

count = 0
for note in [2000,500,100,50,10]:
    count = count + amt // note
    amt = amt % note
print('Minimum number of notes =',count)