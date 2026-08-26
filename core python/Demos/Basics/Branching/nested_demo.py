gender = input("Enter your Gender :")
age = int(input("Enter your age :"))
if (gender =="F" or gender == "f"):
    if age >=18 :
        print("Eligible")
    else:
        print("Not Eligible")
else:
    if age >=21:
        print("Eligible")
    else:
        print("not Eligible")
    