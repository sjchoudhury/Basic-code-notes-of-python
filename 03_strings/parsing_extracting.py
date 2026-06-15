#From jyotichutani@gmail.com sat jan 5 29
# It's useful for finding data & it very much helpful for machine learning.
# atpos = is for 1st position, stpos = is for 2nd position, host = is for printiing the words inside the string
data = 'From jyotichutani@gmail.com sat jan 5 29'
atpos = data.find('@')
print(atpos)
stpos = data.find(" ",atpos)
print(stpos)
host = data[atpos + 1:stpos]
print(host)
str = data[atpos:stpos]
print(str)
