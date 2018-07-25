class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        size = len(nums)
        return max(nums[0] * nums[1] * nums[len(nums) - 1], nums[size - 1] * nums[size - 2] * nums[size - 3])

sol = Solution()
print sol.maximumProduct([-1, 2, -3])
print sol.maximumProduct([-1, -2, -3])
print sol.maximumProduct([-4,-3,-2,-1, 60])
print sol.maximumProduct([9,1,5,6,7,2])