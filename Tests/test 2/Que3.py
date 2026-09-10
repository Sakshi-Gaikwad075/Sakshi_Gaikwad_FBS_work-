# A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing
# for entire field using barbed wire 5 times. Circular section has radius 20m and rectangle
# length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then calculate the total
# cost of fencing the field.


r = 20
l = 50
b = 40
cost = 35
times = 5

perimeter = l + l + b + (3.14 * r)

wire = perimeter * times
T_cost = wire * cost
print('Total cost of fencing =',T_cost)