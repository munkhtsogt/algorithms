class Solution(object):
    def findDuplicate(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		lo = 1
		hi = len(nums) - 1
		
		while lo < hi:
			mid = (lo + hi) / 2
			
			count = 0
			for n in nums:
				if n <= mid:
					count += 1
			
			if count <= mid:
				lo = mid + 1
			else:
				hi = mid
		
		return lo

sol = Solution()
print sol.findDuplicate([1, 2, 4, 3, 2])
