class Solution(object):
	def kthSmallest(self, matrix, k):
		"""
		:type matrix: List[List[int]]
		:type k: int
		:rtype: int
		"""
		result = []
		for i in range(0, len(matrix)):
			for j in range(0, len(matrix[i])):
				result.append(matrix[i][j])
		
		result.sort()
		return result[k - 1] if len(result) >= k-1 else 0
		
	def kthSmallestBS(self, matrix, k):
		lo, hi = matrix[0][0], matrix[len(matrix) - 1][len(matrix[0]) - 1]
		while lo < hi:
			mid = (lo + hi) / 2
			count, j = 0, len(matrix[0]) - 1
			for i in range(0, len(matrix)):
				while j >= 0 and matrix[i][j] > mid: j -= 1
				count += j + 1	
			
			if count < mid:
				lo = mid + 1
			else:
				hi = mid
			
		return lo
		      
        	

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]

matrix2 = [[-5]]

print Solution().kthSmallestBS(matrix, 8)
