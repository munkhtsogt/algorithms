class Solution(object):
	def kSort(self, nums, k):
		for i in range(0, len(nums)):
			j = i
			shift = k
			while j > 0 and nums[j - 1] > nums[j] and shift > 0:
				tmp = nums[j]
				nums[j] = nums[j - 1]
				nums[j - 1] = tmp
				j -= 1
				shift -= 1	

		return nums
		
		

print Solution().kSort([5, 2, 3, 4, 1], 2)
