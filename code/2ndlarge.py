a = []
n=int(3)
for i in range(1,n+1):
    b=int(input("Enter number:"))
    a.append(b)
# add sinle item
a.sort()
# sort the list by default
print("Second largest number is:",a[n-2])
