class Solution(object):
    def isToeplitzMatrix(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: bool
		"""
		for i in range(0, len(matrix) - 1):
			for j in range(0, len(matrix[0]) - 1):
				if matrix[i][j] != matrix[i + 1][j + 1]:
					return False
			
		return True
        

matrix = [
			[1,2,3,4],
			[5,1,2,3],
			[9,5,1,2]
		 ]
print Solution().isToeplitzMatrix(matrix)
