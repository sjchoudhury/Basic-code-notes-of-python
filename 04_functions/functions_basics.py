def myfunction():
    print("Hi")
    print("Whatsup")

myfunction()
print("Not in function")
myfunction()


def sumofnum(a,b):
    print(a+b)

sumofnum(2,3)


def sumofnum(a,b,c):
    print(a+b)
    print(c)

sumofnum(2,3,"camp")



def func(fname,lname):
    print(fname + " " + lname)

func("surya","teja")


#key word arguments
#to print every second value
# *val is for unknown amount of number
def my_code(*val):
    #the val can be anything you wanted to print and the no. starts with 0
    print("the last value " + val[4])

my_code("surya","ron","jan","fun","thu","qwe")


#key word arguments
#for many arguments

def printname(child1,child2,child3):
    print("the last child is child3 " + child3)

printname(child1 = "surya", child2 = "funr", child3 = "nagmri")


def place(country = "India ",state = "peoplemind"):
    print("I am from "+country+""+state)

place("America ","sampl")
place("southafrica ")
place()

#function with return statements
#written statements

def func(X):
    return 2*X

print(func(3))

#when you have no define funtion then put pass so there will be no syntax error
def func1():
    pass
func1()

#recursion- repeatedly doing the same thing
def func(Y):
    print(Y)
    if Y == 12:
        return Y
    return func(2*Y)

print(func(3))


def func1(n):
    if n%3 == 1:
        pass
    else:
        print(n)

func1(9)        
