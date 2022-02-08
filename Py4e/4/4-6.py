#4.6
def computepay(h,r):
    # ( 40 hours * normal rate ) + (( overtime hours ) * time-and-a-half rate)
    if(h>40):
        p = ( 40 * r ) + (( h - 40 ) * 1.5 * r)
        return p
    else:
        p = h * r
        return p

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate per hour: "))

pay = computepay(hours, rate)
print("Pay", pay)