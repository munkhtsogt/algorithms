class Solution(object):
    def findRelativeRanks(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[str]
		"""
		l = sorted(nums)[::-1]
		result = []
		for i in range(0, len(nums)):
			index = l.index(nums[i]) + 1
			if index == 1:
				st = "Gold Medal"
			elif index == 2:
				st = "Silver Medal"
			elif index == 3:
				st = "Bronze Medal"
			else:
				st = str(index)

			nums[i] = st

		return nums
        
        
#["Gold Medal","5","Bronze Medal","Silver Medal","4"]        
print Solution().findRelativeRanks([10])
