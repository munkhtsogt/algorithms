class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def preorder(root):
    if not root: return
    print root.val
    preorder(root.left)
    preorder(root.right)

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        depth = {}

        def dfs(root, lvl):
            if not root: return
            depth[root] = lvl  
            dfs(root.left, lvl + 1)
            dfs(root.right, lvl + 1)
        dfs(root,  0)
        max_depth = max(depth.itervalues())
        def helper(root):
            if not root or depth[root] == max_depth: return root
            L, R = helper(root.left), helper(root.right)
            return root if L and R else L or R
        return helper(root)

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

preorder(Solution().subtreeWithAllDeepest(root))
preorder(Solution().subtreeWithAllDeepest(TreeNode(1)))