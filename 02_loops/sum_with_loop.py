count = 0

for thing in [9,41,12,3,74,15]:
    count = count + thing

print('sum',count)


# for calculating the sum
n = input("Enter Number to calculate sum")
n = int (n)
sum = 0
for num in range(0, n+1, 1):

    if(not (num % 2) == 0):
      sum += num;

print("SUM of odd numbers is: ", sum )
