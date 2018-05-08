class Solution(object):
    def merge(self, nums1, m, nums2, n):
		"""
		:type nums1: List[int]
		:type m: int
		:type nums2: List[int]
		:type n: int
		:rtype: void Do not return anything, modify nums1 in-place instead.
		"""
		i, j, end = m - 1, n - 1, m + n - 1
		while i >= 0 and j >= 0:
			if nums2[j] > nums1[i]:
				nums1[end] = nums2[j]
				j -= 1
			else:
				nums1[end] = nums1[i]
				i -= 1
			end -= 1

		for k in range(0, j + 1):
			nums1[k] = nums2[k]

		print nums1		
        
        
Solution().merge([1, 2, 3, 0, 0, 0], 3, [0, 1, 2], 3)
