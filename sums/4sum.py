'''
TIME COMPLEXITY: O(n^3)
'''
class Solution(object):
    def fourSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		nums.sort()
		result = []
		size = len(nums)
		for i in range(0, size - 3):
			if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target: break
			if nums[i] + nums[size - 1] + nums[size - 2] + nums[size - 3] < target:	continue
			if i > 0 and nums[i] == nums[i - 1]: continue
			for j in range(i + 1, size - 2):
				if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target: break
				if nums[i] + nums[j] + nums[size - 1] + nums[size - 2] < target:	continue
				if j > i + 1 and nums[j] == nums[j - 1]: continue
				l = j + 1
				r = size - 1
				while l < r:
					s = nums[i] + nums[j] + nums[l] + nums[r]
					if s == target:
						result.append([nums[i], nums[j], nums[l], nums[r]])
						while l < r and nums[l] == nums[l + 1]: l += 1
						while l < r and nums[r] == nums[r - 1]: r -= 1
						l += 1
						r -= 1
					elif s > target:
						r -= 1
					else:
						l += 1

		return result
        	

print Solution().fourSum([1, 0, -1, 0, -2, 2], 0)
