'''
TIME COMPLEXITY: O(n^2)
'''
class Solution(object):
    def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		nums.sort()
		result = []
		for i in range(0, len(nums) - 2):
			if i > 0 and nums[i] == nums[i - 1]:
				continue
			j = i + 1
			k = len(nums) - 1
			while j < k:
				s = nums[i] + nums[j] + nums[k]
				if s == 0:
					result.append([nums[i], nums[j], nums[k]])
					while j < k and nums[j] == nums[j + 1]: j += 1
					while j < k and nums[k] == nums[k - 1]: k -= 1
					j += 1
					k -= 1
				elif s > 0:
					k -= 1
				else:
					j += 1

		return result

print Solution().threeSum([-1,0,1,2,-1,-4])
