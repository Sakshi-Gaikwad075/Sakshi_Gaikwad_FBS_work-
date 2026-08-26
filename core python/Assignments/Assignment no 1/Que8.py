# W.P. to convert days into years,weeks and days

days = int(input("enter number of days:"))

years = days // 365
remainder_days = days % 365

weeks = remainder_days // 7
days = remainder_days % 7

print("Years =",years)
print("weeks =",weeks)
print("days =",days)