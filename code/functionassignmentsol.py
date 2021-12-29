def computeTotalpay(days, rate):
pay = days * rate
return pay

xh = input("Enter Days:")

xr = input("Enter Rate:")


try:
fh = float(xh)
fr = float(xr)

print("Pay: ",computeTotalpay(fh,fr))
except:
print("Error, please enter numeric input")
#
