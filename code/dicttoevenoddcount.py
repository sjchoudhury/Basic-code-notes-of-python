# to count Even
# and Odd numbers in a List

# list of numbers
list1 = [1,2,3,4,5,6,7,8,9,10]
even_count, odd_count = 0, 0

for num in list1:

    if num % 2 == 0:
        even_count += 1

    else:
        odd_count += 1

print("Even:", even_count)
print("Odd:", odd_count)

# printing the length of `my_list`
#print({"print1", "print2"})
d = {("Even:", even_count,
     "Odd:", odd_count)}
print(d)
