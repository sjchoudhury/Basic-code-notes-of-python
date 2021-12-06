
a = int(input("Enter a number"))
b = int(input("Enter a number"))
c = int(input("Enter a number"))

large = -1
for i in [a,b,c]:
     if i > large:
        large = i

print('largest number',large)
