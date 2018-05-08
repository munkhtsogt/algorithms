# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys

class Solution(object):
    def minDepth(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if root == None: return 0
		self.minDepth = sys.maxint
		def traverse(node, depth):
	
			if node == None:
				return

			if not node.left and not node.right:
				self.minDepth = min(self.minDepth, depth)	
	
			if node.left:
				traverse(node.left, depth + 1)
		
			if node.right:
				traverse(node.right, depth + 1)

		traverse(root, 0)
		return self.minDepth
        
        
