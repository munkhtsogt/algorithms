# Reverse in order traverse.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.total = 0
    
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def inorder(root):
            if not root: return
            inorder(root.right)
            self.total += root.val
            root.val = self.total
            inorder(root.left)
        
        inorder(root)
        return root



root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(13)

sol = Solution()
root = sol.convertBST(root)