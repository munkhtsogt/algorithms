class Solution(object):
	def missingNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums) == 0: return 0
		if len(nums) == 1: return 0 if nums[0] == 1 else nums[0] + 1
		nums.sort()
		lo, hi = 0, len(nums)
		while lo < hi:
			mid = lo + (hi - lo) / 2
			if nums[mid] > mid:
				hi = mid
			else:
				lo = mid + 1
	
		return lo
	
	def missingNumber2(self, nums):
		n = len(nums)
		return n * (n + 1) / 2 - sum(nums)
       	


print Solution().missingNumber2([3, 0, 1]) 
       
