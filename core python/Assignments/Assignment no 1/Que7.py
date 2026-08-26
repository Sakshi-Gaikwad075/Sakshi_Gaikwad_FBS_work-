# find roots of quadratic equation

import math

a = float(input("Enter value of a:"))
b = float(input("Enter value of b:"))
c = float(input("Enter value of c:"))

d = b*b - 4*a*c

root1 = (-b + math.sqrt(d)) / (2*a)
root2 = (-b - math.sqrt(d)) / (2*a)

print("Root 1 =", root1)
print("Root 2 =", root2)