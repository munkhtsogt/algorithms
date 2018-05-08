class Solution(object):
    def subsets(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		subsets = [[]]
		for n in nums:
			subsets += [ s + [n] for s in subsets]
		return subsets	
        
        

print Solution().subsets([1, 2, 3, 4])
