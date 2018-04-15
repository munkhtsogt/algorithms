class Solution(object):
    def thirdMax(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		nums = list(set(nums))
		nums.sort(reverse=True)
		return nums[2] if len(nums) >= 3 else nums[0]

print Solution().thirdMax([2, 1])
