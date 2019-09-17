# This program takes meal prices, and rounds up the total price to include a tip.
# 9/16/29
# CTI-110 P2HW1 - Meal Tip Tax Calculator
# Jonnie leaf



#input food price
meal=float(input("enter meal price: $"))
#input tip percentage, and then the code converts the percentage to decimal form
tip=float(input("enter tip percentage: "))
tipp=0.01*tip*meal
#input tax rate, and then the code converts the percentage to decimal form
tax=float(input("enter tax percentage: "))
taxx=0.01*tax*meal
#calculates purchase total
total=meal+tipp+taxx
print("your total meal price is $",total)
input()
