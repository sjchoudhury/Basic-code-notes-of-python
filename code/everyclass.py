#range
for i in range (1,100):
    print(i)

num1 = int(input("lower value is"))
num2 = int(input("upper value is"))
for _ in range(num1,num2):

    print(_)
print(num2)

#num1 = int(input("lower value is"))
num2 = int(input("upper value is"))
for _ in range(num2):#1

    print(_,end="\t")#1
print(num2)#5


#for loop of string
st = "python"
for i in st:
    print(i,end=" ")



num = float(input("Enter a number"))
if num % 2 == 0:
    print("Zero")
else:
        print("positive number")
