class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 

        nums.sort()

        median = nums[len(nums) / 2]
        move = 0
        for i in range(len(nums)):
            move += abs(median - nums[i])

        return move

print Solution().minMoves2([1, 2, 3, 3, 3])