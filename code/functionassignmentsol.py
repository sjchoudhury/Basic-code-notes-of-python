#Rewrite your pay computation and create a function called compute Total pay which takes two parameters (days and rate) and returns computed pay as answer
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
