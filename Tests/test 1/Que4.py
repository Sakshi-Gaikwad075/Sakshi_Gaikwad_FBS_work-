area = float(input("Enter area of one wall:"))
in_cost = float(input('Enter interior painting cost per sq.ft :'))
ex_cost = float(input('Enter exterior painting coest per sq.ft :'))

in_area = area * 2
ex_area = area * 6

interior_total = in_area * in_cost
exterior_total = ex_area * ex_cost

total_cost = interior_total + exterior_total
print('Interior painting cost =', interior_total)
print('Exterior painting cost =',exterior_total)
print('Total painting cost =',total_cost)