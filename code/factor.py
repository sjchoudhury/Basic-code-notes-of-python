#
# Python Program to find the factors of a number

# for finding out the factors of all entered bumbers

def print_factors(x):

   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = int(input("Enter the number for finding the factor"))

print_factors(num)
