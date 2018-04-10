class Solution(object):
    def findDisappearedNumbers(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		r = [-1] * len(nums)
		for num in nums:
			r[num - 1] = num - 1

		
		return [ i + 1 for i in range(0, len(r)) if r[i] == -1 ]
    	
sol = Solution()
print sol.findDisappearedNumbers([4,3,2,7,8,2,3,1])
        
        
