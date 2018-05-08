# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
    def averageOfLevels(self, root):
		"""
		:type root: TreeNode
		:rtype: List[float]
		"""

		def helper(node, levels, level):
			if node == None:
				return
	
			if level not in levels:
				levels[level] = [node.val]
			else:
				levels[level].append(node.val)
	
			helper(node.left, levels, level + 1)
			helper(node.right, levels, level + 1)

		levels = {}
		helper(root, levels, 0)
		
		r = []
		for k in levels:
			v = levels[k]
			r.append(float(sum(v)) / len(v))
		
		return r
        
        
        

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print Solution().averageOfLevels(root)
