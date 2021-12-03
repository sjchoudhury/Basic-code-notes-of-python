# calculator

x = int(input("Enter the number:"))
y = int(input("Enter the number:"))

def divide(x,y):
#for divide
    return x / y

def multiply(x,y):
#for multiplying
    return x * y

def add(x,y):
#for adding
    return x + y

def subtract(x,y):
#for subtracting
    return x - y


print("Select the operation")
print("A. divide")
print("B. multiply")
print("C. add")
print("D. subtract ")

operation = input("choose the operation(A/B/C/D):")


if operation == 'A':
    print(x,"/",y,"=",divide(x,y))

elif operation == 'B':
    print(x,"*",y,"=",multiply(x,y))

elif operation == 'C':
    print(x,"+",y,"=",add(x,y))

elif operation == 'D':
    print(x,"-",y,"=",subtract(x,y))

else:
    print("This is a invalid input")
