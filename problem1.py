'''
Given an array of integers arr, youre asked to calculate for each index i the product of all integers except the integer at that index (i.e. except arr[i]). Implement a function arrayOfArrayProducts that takes an array of integers and returns an array of the products.

Solve without using division and analyze your solutions time and space complexities.

Examples:

input:  arr = [8, 10, 2]
output: [20, 16, 80] # by calculating: [10*2, 8*2, 8*10]

input:  arr = [2, 7, 3, 4]
output: [84, 24, 56, 42] # by calculating: [7*3*4, 2*3*4, 2*7*4, 2*7*3

2. All paths of BST
3. 111111 + 1010101
4. longest path of BST

'''

def calcProduct(arr):	
	l = len(arr)
	result = [1] * l
	j, k = 1, 1
	for i in range(0, l):
		if i > 0:
			j = j * arr[i - 1]
			result[i] *= j
			k = k * arr[l - i]
			result[l - 1 - i] *= k
			
	return result

print calcProduct([2, 3, 4, 5, 6])

