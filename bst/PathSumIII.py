# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
			
class Solution(object):
	def pathSum(self, root, sum):
		"""
		:type root: TreeNode
		:type sum: int
		:rtype: int
		"""
		self.path = 0
		def traverse(node, total, sum, parentUsed):
			if not node:
				return 	

			total += node.val
			
			if total == sum:
				self.path += 1

			if node.left:
				traverse(node.left, total, sum, True)
				if not parentUsed:
					traverse(node.left, 0, sum, False)	

			if node.right:
				traverse(node.right, total, sum, True)
				if not parentUsed:
					traverse(node.right, 0, sum, False)
					
		traverse(root, 0, sum, False)	
		return self.path
		
#[1,-2,-3,1,3,-2,null,-1] -1
root = TreeNode(1)
root.left = TreeNode(-2)
root.right = TreeNode(-3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(-2)
root.left.left.left = TreeNode(-1)

print Solution().pathSum(root, -1)
