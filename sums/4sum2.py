'''
TIME COMPLEXITY: O(n^2)
'''
class Solution(object):
    def fourSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		data = {}
		for i in range(0, len(nums)):
			for j in range(i + 1, len(nums)):
				s = nums[i] + nums[j]
				if s not in data:
					data[s] = [(i, j)]
				else:
					data[s].append((i, j))
		result = set()	
		for k in data:
			if target - k in data:
				list1 = data[target - k]
				list2 = data[k]
				for (i, j) in list1:
					for (l, m) in list2:
						list3 = [i, j, l, m]
						if len(set(list3)) != len(list3): continue
						list4 = [nums[i], nums[j], nums[l], nums[m]]
						list4.sort()
						result.add(tuple(list4))	
	
		return list(result)
		
print Solution().fourSum([1, 0, -1, 0, -2, 2], 0)
