# Program to multiply two matrices using nested loops

# take a 3x3 matrices
A = ([[2, 3, 5],
      [4, 5, 6],
	  [4, 2, 3]])

# take a 3x3 matrix
B = ([[2, 4, 7],
	  [3, 5, 1],
	  [3, 6, 2]])

matrix = []


result = [[0, 0, 0],
		[0, 0, 0],
		[0, 0, 0]]
print(A),        print(B)
# iterating by row of A
for i in range(len(A)):

	# iterating by column by B
	for j in range(len(B[0])):

		# iterating by rows of B
		for k in range(len(B)):
			result[i][j] += A[i][k] * B[k][j]
print('Product matrix be like')
for r in result:
	print(r)
