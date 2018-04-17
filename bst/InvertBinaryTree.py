#Google: 90% of our engineers use the software you wrote (Homebrew), 
#        but you can’t invert a binary tree on a whiteboard so f*** off. by Max Howell
class Solution(object):
	def invertTree(self, root):
		"""
		:type root: TreeNode
		:rtype: TreeNode
		"""
		if root:
			left = self.invertTree(root.left)
			right = self.invertTree(root.right)
			root.left = right
			root.right = left
	
		return root
	
	def invertTree2(self, root):
		"""
		:type root: TreeNode
		:rtype: TreeNode
		"""
		if root:
			left = root.left
			root.left = root.right
			root.right = left
			self.invertTree2(root.left)
			self.invertTree2(root.right)
	
		return root
			        
        
