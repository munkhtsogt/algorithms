# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""

		def traverse(node):
			if node == None:
				return 0
			
			if node.left != None and node.left.left == None and node.left.right == None:
				return node.left.val + traverse(node.right)
			
			l = traverse(node.left)
			r = traverse(node.right)	

			return l + r

		return traverse(root)
        
