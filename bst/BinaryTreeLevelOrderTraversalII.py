# Definition for a binary tree node.
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
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        results = []
        result = {}
        def helper(root, height):
            if root == None: return

            if height not in result:
                result[height] = []
            
            result[height].append(root.val)

            helper(root.left, height + 1)
            helper(root.right, height + 1)    

        helper(root, 0)
        for i in range(len(result.values()) - 1, -1, -1):
            results.append(result.values()[i])

        return results
        


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sol = Solution()
print sol.levelOrderBottom(root)
print sol.levelOrderBottom(None)

        

