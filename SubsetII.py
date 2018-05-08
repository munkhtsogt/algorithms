class Solution(object):
    def subsetsWithDup(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""

		def backtrack(nums, result, tmp, start):
			result.append(tmp[:]) # copy of tmp
			for i in range(start, len(nums)):
				if i > start and nums[i - 1] == nums[i]: continue
				tmp.append(nums[i])
				backtrack(nums, result, tmp, i + 1)
				tmp.pop()
	

		result = []
		nums.sort()
		backtrack(nums, result, [], 0)
		return result
        

print Solution().subsetsWithDup([4, 4, 4, 1, 4])
