# Finding the largest value
largest_so_far = -1
print('Before', the largest_so_far)
for the_num in [78,34,56,97,23]:
   if the_num > largest_so_far:
       largest_so_far = the_num
    print(largest_so_far,the_num)

print('After',largest_so_far)



# other type

a = int(input("Enter a number "))
b = int(input("Enter a number "))

large = -1
for i in [a,b]:
     if i > large:
        large = i

print('largest number',large)
