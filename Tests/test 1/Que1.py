# area and perimeter of given figure
import math
l = float(input("Enter length :"))
b = float(input("Enter breadth :"))
r = float(input("Enter radius :"))

# area of rectangle
area_rect = l * b

# area of semicircle
area_semi = (math.pi * r * r)/2

# total area
area = area_rect + area_semi

# perimeter 
perimeter = (2 * l) + (math.pi * r)

print(f'Area = {area}.')
print(f'Perimeter ={perimeter}.')