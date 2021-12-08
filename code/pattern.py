# pattern printing

#
# #
# # #
# # # #

#nested loops
rows = 4
# outer loop
for j in range(1, rows+1):
    print("# " * j)

# or

n = int(input("num"))
i = 1
while i <= n:
    j = 1
    while j <= i:
        print("# ",end="")
        j = j + 1# or we can write j +=1
    print()
    i+=1
# for another design
#
# #
# # #
# # # #
j = 1
while j <= 4:
    i = 1
    while i <= j:
        print("# ",end =" ")
        i = i + 1
    print()
    j = j + 1

# for opposite

j = 4
while j >= 1:
    i = 1
    while i <= j:
        print("# ",end =" ")
        i = i + 1
    print()
    j = j - 1
