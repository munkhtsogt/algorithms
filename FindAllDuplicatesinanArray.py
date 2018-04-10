class Solution(object):
    def findDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		data = {}
		results = []
		for num in nums:
			if num not in data:
				data[num] = 1
			else:
				data[num] += 1
				if data[num] != 1:
					results.append(num)

		return results

sol = Solution()
print sol.findDuplicates([4,3,2,7,8,2,3,1])
        
        
