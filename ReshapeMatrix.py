class Solution(object):
    def matrixReshape(self, nums, r, c):
		"""
		:type nums: List[List[int]]
		:type r: int
		:type c: int
		:rtype: List[List[int]]
		"""

		if len(nums) == 0 or r * c > len(nums) * len(nums[0]):
			return nums

		re = [[0] * c for i in range(0, r)]
		k, l = 0, 0
		for i in range(0, r):
			for j in range(0, c): 
				if l < len(nums[k]):
					re[i][j] = nums[k][l]
				else:
					k += 1
					l = 0
					re[i][j] = nums[k][l]
				l += 1

		return re
        

nums = [[1,2],[3,4]]
print Solution().matrixReshape(nums, 1, 4)
