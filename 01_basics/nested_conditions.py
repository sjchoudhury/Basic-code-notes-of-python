num = float(input("Enter a number"))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("positive number")
else:
    print("Negative number")

#

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
