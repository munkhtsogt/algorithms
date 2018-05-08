class Solution(object):
    def findShortestSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		left, right, count = {}, {}, {}
		for i, e in enumerate(nums):
			if e not in left: left[e] = i
			right[e] = i
			count[e] = count.get(e, 0) + 1	
		
		r = len(nums)
		degree = max(count.values())
		for e in count:
			if count[e] == degree:
				r = min(r, right[e] - left[e] + 1)
		
		return r
		
		
		

print Solution().findShortestSubArray([1,2,2,1,2,1,1,1,1,2,2,2])
