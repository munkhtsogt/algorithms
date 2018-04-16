'''
TIME COMPLEXITY: O(n)
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result, check = [], {}
        for i in range(0, len(nums)):
        	if target - nums[i] in check:
        		d = target - nums[i]
        		result.append(check[d])
        		result.append(i)
        		break
        	check[nums[i]] = i
        	 	
        return result
        

print Solution().twoSum([2, 7, 11, 15], 17)
