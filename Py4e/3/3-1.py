# 3.1 Write a program to prompt the user for hours 
# and rate per hour using input to compute gross pay.
# if-else, try-except

try:
    hours = float(input("Enter Hours:"))
    rate = float(input("Enter Rate per hour:"))
except:
    print("Error, Please enter a numeric input.")
    quit()

overtime = rate*1.5

if(hours <= 40):
    print(hours*rate)
elif(hours > 40):
    print(((hours-40)*overtime)+(40*rate))