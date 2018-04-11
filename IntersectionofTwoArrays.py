class Solution(object):
    def intersect(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: List[int]
		"""
		if not nums1 and nums2:
			return []
			
		data = {}
		for num in nums1:
			if num not in data:
				data[num] = 1

		result = []
		for num in nums2:
			if num in data and data[num] != 0:
				result.append(num)
				data[num] -= 1
		return result
        

sol = Solution()
print sol.intersect([1, 2, 2, 1], [2, 2])
