# Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:
xh = input("Enter Days:")
xr = input("Enter Rate:")
try:
    fh = float(xh)
    fr = float(xr)
except:
      print("Error, please enter numeric input")
#
