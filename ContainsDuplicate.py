class Solution(object):
    def containsDuplicate(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""	
		return len(nums) != len(set(nums))	
        

sol = Solution()
print sol.containsDuplicate([1, 2, 1])
