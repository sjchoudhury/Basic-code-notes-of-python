# Take the following Python code that stores a string:`str = 'Perfect-Plan-B:0.7541' Use find and string slicing to extract the portion of the string after the colon (:) character and then use the float function to convert the extracted string into a floating point number.
str = 'Perfect-Plan-B:0.7541'
atpos = str.find(':')
num = str[(atpos+1):]
float_num = float(num)
print(float_num)
