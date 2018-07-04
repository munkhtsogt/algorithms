# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        def helper(root, k, s):
            if not root: return False
            if k - root.val in s: return True
            s.add(root.val)
            return helper(root.left, k, s) or helper(root.right, k, s)

        return helper(root, k, set())


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)

sol = Solution()
print sol.findTarget(root, 9)
print sol.findTarget(root2, 4)