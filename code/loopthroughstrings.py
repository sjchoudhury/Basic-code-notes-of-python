# these are for looping through strings
# both code 1 & 2 are for same output
# code1
string_name = "perfectplanb"

#iterate over the string
for element in string_name:
    print(element)
print("\n")# is for new line

#code2
#iterate over index
for element in range (0,len(string_name)):
    print(string_name[element])
# element is just a variaable
print("\n")

word = string_name
count = 0 #Initial value of count
for letter in word:
    if letter == 'p' :
        count = count + 1 #Incrementing each time letter ' 'comes
print(count)
