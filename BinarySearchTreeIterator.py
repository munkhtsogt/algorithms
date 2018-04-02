# Definition for a  binary tree node
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class BinarySearchTree(object):
	def __init__(self):
		self.root = None
	
	def getRoot(self):
		return self.root
	
	def add(self, x):
		if self.root:
			self.insert(x, self.root)
		else:
			self.root = TreeNode(x)
	
	def insert(self, x, leaf):
		if x < leaf.val:
			if leaf.left:
				self.insert(x, leaf.left)
			else:
				leaf.left = TreeNode(x)
		else:
			if leaf.right:
				self.insert(x, leaf.right)
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
		

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.results = []
        self.index = 0
        while len(self.stack) != 0 or root != None:
        	if root != None:
        		self.stack.append(root)
        		root = root.left
    		else:
    			root = self.stack[-1]
    			self.stack.pop()
    			self.results.append(root.val)
    			root = root.right
        	
    def hasNext(self):
		"""
		:rtype: bool
		"""
		if self.index < len(self.results):
			return True
		else:
			return False
		
    def next(self):
        """
        :rtype: int
        """
        i = self.index
        self.index += 1
        return self.results[i]
        
bst = BinarySearchTree()
bst.add(10)
bst.add(8)
bst.add(11)
bst.add(5)
bst.add(9)
bst.add(4)
bst.add(6)
#bst.inorder()
#bst.preorder()
#bst.postorder()
#bsti = BSTIterator(bst.getRoot())
# Your BSTIterator will be called like this:
i, v = BSTIterator(bst.getRoot()), []
while i.hasNext(): v.append(i.next())

