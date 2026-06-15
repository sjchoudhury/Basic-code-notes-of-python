def Check_Vow(string, vowels):
    final = [each for each in string if each in vowels]
    print(final)

# Driver Code
string = input("Enter any sentence ")
vowels = "AaEeIiOoUu"
Check_Vow(string, vowels);
