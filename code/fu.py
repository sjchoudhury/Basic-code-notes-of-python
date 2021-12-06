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


i = 2
while True:
    if i%3 == 0:
        break
    print(i)
    i += 2
