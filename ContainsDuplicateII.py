class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: bool
		"""
		data = {}
		for i in range(0, len(nums)):
			if nums[i] in data and abs(i - data[nums[i]]) <= k:
				return True
			data[nums[i]] = i

		return False	
        
sol = Solution()
print sol.containsNearbyDuplicate([1, 0, 1, 1], 1)
