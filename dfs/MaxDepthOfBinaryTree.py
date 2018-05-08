# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
        	return 0
    	
    	depth = 0
    	if root.left:
    		depth = max(depth, self.maxDepth(root.left))
    	
    	if root.right:
    		depth = max(depth, self.maxDepth(root.right))
    	
    	return depth + 1
        
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print Solution().maxDepth(root)
