# W.P. enter p,r,t and calculate C.I
P = float(input("Enter amount:"))
R = float(input("Enter rate of interst:"))
T = float(input("Enter time:"))

A = P * ( 1 + R/100) ** T
CI = A - P

print(f"Compound interest on amount {P} is {CI}.")