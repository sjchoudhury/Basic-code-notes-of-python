# this is by mixing calculator block code and condition block code

def divide(x, y):
    # for divide
    return x / y

def multiply(x, y):
    # for multiplying
    return x * y

def add(x, y):
    # for adding
    return x + y

def subtract(x, y):
    # for subtracting
    return x - y

def sign(num):
    if num > 0:
        return "Positive"
    elif num == 0:
        return "Zero"
    elif num < 0:
        return "Negative"

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

print("Select the operation:")
print("A. Divide")
print("B. Multiply")
print("C. Add")
print("D. Subtract")
print("E. Determine sign of a single number")

operation = input("Choose the operation (A/B/C/D/E): ")

if operation == 'A':
    print(x, "/", y, "=", divide(x, y))
elif operation == 'B':
    print(x, "*", y, "=", multiply(x, y))
elif operation == 'C':
    print(x, "+", y, "=", add(x, y))
elif operation == 'D':
    print(x, "-", y, "=", subtract(x, y))
elif operation == 'E':
    num = float(input("Enter a number: "))
    print(sign(num))
else:
    print("Invalid input")
