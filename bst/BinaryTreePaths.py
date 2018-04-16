class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class BinaryTree(object):
	def __init__(self):
		self.root = None

	def getRoot(self):
		return self.root
	
	def add(self, x):
		if self.root:
			self._add(self.root, x)
		else:
			self.root = TreeNode(x)	

	def _add(self, leaf, x):
		if x < leaf.val:
			if leaf.left:
				self._add(leaf.left, x)
			else:
				leaf.left = TreeNode(x)
		else:
			if leaf.right:
				self._add(leaf.right, x)
			else:
				leaf.right = TreeNode(x)

	def inorder(self):
		self.inorderTraverse(self.root)

	def preorder(self):
		self.preorderTraverse(self.root)

	def postorder(self):
		self.postorderTraverse(self.root)			

	def inorderTraverse(self, leaf):
		if leaf:
			self.inorderTraverse(leaf.left)
			print leaf.val
			self.inorderTraverse(leaf.right)

	def preorderTraverse(self, leaf):
		if leaf:
			print leaf.val
			self.preorderTraverse(leaf.left)
			self.preorderTraverse(leaf.right)
		
	def postorderTraverse(self, leaf):
		if leaf:
			self.postorderTraverse(leaf.left)
			self.postorderTraverse(leaf.right)
			print leaf.val	

class Solution(object):
	def binaryTreePaths(self, root):
		"""
		:type root: TreeNode
		:rtype: List[str]
		"""
		def traverseTree(leaf, results, path):
			if leaf == None:
				return
				
			if leaf.left == None and leaf.right == None:
				results.append(path + str(leaf.val))
				
			path += str(leaf.val)
			if leaf.left:
				traverseTree(leaf.left, results, path + "->")
			
			if leaf.right:
				traverseTree(leaf.right, results, path + "->")	
			
		results = []
		traverseTree(root, results, "")
		
		return results

bt = BinaryTree()
bt.add(1)
bt.add(2)
bt.add(3)
bt.add(5)
#bt.inorder()
sol = Solution()
print sol.binaryTreePaths(bt.getRoot())     
        
