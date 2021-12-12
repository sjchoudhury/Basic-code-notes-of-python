#n = int(input("Enter a number"))
#if n % 3 == 0:
#    print("Fizz")
#if n % 5 == 0:
#    print("Buzz")
##    print("Fizz-Buzz")


n = int(input("Enter a number "))
s = ""
if n % 3 == 0:
    s += "Fizz"
if n % 5 == 0:
    s += "Buzz"
else:
    print(n)
print(s)
