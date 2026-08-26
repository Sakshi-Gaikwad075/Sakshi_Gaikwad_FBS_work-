# convert distance feet, inches into meter, centimeter

# 1 foot == 0.3048
# 1 inch == 2.54

# input distance in feet and inches
f = int(input("Enter distance in feet:"))
i = int(input("Enter distance in inches:"))

# convert in meter and centimeter
m = f* 0.3048
cm = i * 2.54
print(f"distance in meter is: {m} & distance in centimeter is : {cm}")