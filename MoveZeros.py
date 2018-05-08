class Solution(object):
    def moveZeroes(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		zeros = 0
		for i in range(0, len(nums)):
			if nums[i] == 0:
				zeros += 1
			elif zeros != 0:
				nums[i - zeros] = nums[i]
				nums[i] = 0

		print nums
sol = Solution()
sol.moveZeroes([1, 1, 1, 1, 0])
