import sys
n = 5
m = 6
matrix = [[0] * m for i in range(n)]

for i in range(n):
	for j in range(m):
		sys.stdout.write(str(matrix[i][j]) + " ")
		sys.stdout.flush()
	print
