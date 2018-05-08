import sys
class Solution(object):
    def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		best, sum = -sys.maxint, 0
		for i in range(len(nums)):
			sum = max(nums[i], sum + nums[i])
			best = max(best, sum)
		return best
		
print Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
