# finding the smallest value
small = None
for i in [1,33,312,1,2,3,5,]:
    if small is None:
        small = i
    elif i<small:
        small = 1

print("smallest value:",small)
#
