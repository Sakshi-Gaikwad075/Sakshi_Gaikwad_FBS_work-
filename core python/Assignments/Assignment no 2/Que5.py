# W A P to calculate selling price of based on cost price and discount
cp = int(input("Enterr Cost Prise :"))
d = int(input("enter discount:"))

dis_amt = cp * d / 100
sp = cp - dis_amt
print("Selling price =", sp)