# convert time in hh,min,sec into seconds
h = int(input("Enter hours:"))
m = int(input("Enter minutes:"))
sec = int(input("Enter seconds:"))

total = (h * 3600) + (m * 60) + sec

print("total seconds =",total)