class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def max_i(nums):
            max, index = 0, 0
            for i in range(len(nums)):
                if nums[i] > max: 
                    max = nums[i]
                    index = i
            
            return index

        def helper(nums):
            if len(nums) == 0: return None
            i = max_i(nums)
            root = TreeNode(nums[i])
            root.left = helper(nums[:i])
            root.right = helper(nums[i + 1:])
            return root

        return helper(nums)


print Solution().constructMaximumBinaryTree([3,2,1,6,0,5])   