# all " i " are rows
# all '" j "' are column
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

j = 1
while j <= 4:
    i = 1
    while i <= j:
        print("# ",end =" ")
        i = i + 1
    print()
    j = j + 1


# patterns with numbers
# for n is a startin value & o is ending valuse
n = 9 # n can be any numbers
for row in range(n,0,-1):
    for col in range(1,row+1 ):
        print(col ,end=" ")
    print()

# for opposite
n = 10 # n can be any numbers
for row in range(0,n,+1):
    for col in range(1,row+1 ):
        print(col ,end=" ")
    print()


# for pattern with not repeating same number
n = int(input())
val = 1
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(val,end=" ")
        val += 1
    print()

# for space in between two lines of patterns

j = 1
while j <= 5:
    i = 1
    while i <= j:
        print("*",end ="")
        i = i + 1
    print()
    print()
    j = j + 1

    #@title
def halfDiamondStar(N):
    for i in range(N):

        for j in range(0, i+1):
            print("*", end = "")
        print()


    for i in range(1, N):

        for j in range(i, N):
            print("*", end = "")
        print()


N = 5;


halfDiamondStar(N);
  
