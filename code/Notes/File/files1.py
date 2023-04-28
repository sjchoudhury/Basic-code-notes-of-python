# READ WHOLE FILE

# File handle

f = open('file.txt')
for var in f:
    print(var)

# for printing the numbers of line
f  = open('file.txt')
count = 0
for var in f:
    count = count + 1
print("line count", count)


# reading the whole file as a string - for industrial purposes

fhand = open('file.txt')
stringinput = fhand.read()
print(len(stringinput))
# whole length
print(stringinput[:20])
#first 20 characters

# for finding anything in the File
if "file" in stringinput:
    print("yes")


f = open('file.txt')

stringinput= f.read()
repeated = stringinput.count("file")
print("times of repeated file word", repeated)
