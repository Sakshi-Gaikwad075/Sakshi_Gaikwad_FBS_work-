p1 = float(input('Enter price of 1st product:'))
p2 = float(input('Enter price of 2st product:'))
p3 = float(input('Enter price of 3st product:'))
p4 = float(input('Enter price of 4st product:'))
p5 = float(input('Enter price of 5st product:'))

total = p1 + p2 + p3 + p4 + p5

gst = total * 18/100
bill = total + gst
print('Total bill =',bill)