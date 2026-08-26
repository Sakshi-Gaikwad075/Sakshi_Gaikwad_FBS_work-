# W.P.to enter P,T,R and calculate S.I

P = int(input("Enter amount:"))
R = int(input("Enter rate of interst:"))
T = int(input("Enter time:"))

S_I = P*R*T/100
print(f"simple Interest on amount {P} is {S_I}")