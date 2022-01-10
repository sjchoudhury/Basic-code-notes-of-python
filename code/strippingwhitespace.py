# it is for stripping of whitespaces of any input from right side or from left side or else from both sides
# lstrip() -  is for slicing the left side of whitespaces
# rstrip() - is for slicing the right side of whitespaces

s = '  Hellobob   '
print(s.lstrip())
print(s.lstrip())
print(s.strip())
print(s)



s1 = '  abc  '

print(f'String =\'{s1}\'')

print(f'After Removing Leading Whitespaces String =\'{s1.lstrip()}\'')

print(f'After Removing Trailing Whitespaces String =\'{s1.rstrip()}\'')

print(f'After Trimming Whitespaces String =\'{s1.strip()}\'')
