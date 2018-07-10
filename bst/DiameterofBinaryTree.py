# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.result = 1
        def dfs(root):
            if not root: return 0
            L = dfs(root.left)
            R = dfs(root.right)
            self.result = max(self.result, L + R + 1)
            return max(L, R) + 1

        dfs(root)
        return self.result - 1


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print Solution().diameterOfBinaryTree(root)
print Solution().diameterOfBinaryTree(TreeNode(1))
