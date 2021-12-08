# Python program to remove vowels from a string
# Function to remove vowels
def rem_vowel(string):
	vowels = ['a','e','i','o','u']
	result = [letter for letter in string if letter.lower() not in vowels]
	result = ''.join(result)
	print(result)

# Driver program
string = input("Enter any sentence ")
rem_vowel(string)
