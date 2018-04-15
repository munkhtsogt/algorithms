# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
		"""
		:type root: TreeNode
		:type sum: int
		:rtype: bool
		"""

		def helper(node, s, sum):
			if node == None:
				return False
		
			if node.left == None and node.right == None:
				return s + node.val == sum 

			return helper(node.left, s + node.val, sum) or helper(node.right, s + node.val, sum)	

		return helper(root, 0, sum) 
        
        

sol = Solution()
print sol.hasPathSum()
