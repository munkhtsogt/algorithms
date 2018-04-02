class Solution(object):
    def findMin(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		lo, hi = 0, len(nums) - 1
		while lo < hi:
			mid = (lo + hi) >> 1
			if nums[lo] < nums[hi]:
				return nums[lo]
			
			if nums[mid] > nums[hi]:
				lo = mid + 1
			else: 
				hi = mid
			
		return nums[lo]

sol = Solution()
print sol.findMin([4, 5, 6, 7, 0, 1, 2])
