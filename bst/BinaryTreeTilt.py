# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
    def findTilt(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""

		self.s = 0
		def helper(node):
			if not node:
				return 0			

			l = helper(node.left)
			r = helper(node.right)
			self.s += abs(l - r)
		
			return node.val + l + r

		helper(root)
		return self.s
		
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print Solution().findTilt(root)
