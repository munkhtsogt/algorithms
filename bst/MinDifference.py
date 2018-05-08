class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

import sys		
class Solution(object):
    def getMinimumDifference(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		self.min = sys.maxint
		self.prev = None
		def inorder(node):
			if not node:
				return
	
			inorder(node.left)
			if self.prev:
				self.min = min(self.min, abs(node.val - self.prev.val))
			
			self.prev = node
			inorder(node.right)

		inorder(root)
		return self.min
        

root = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(2)

print Solution().getMinimumDifference(root)
