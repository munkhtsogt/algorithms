# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        if not s: return False

        def helper(s, t):
            if not s and not t: return True
            if not s or not t: return False
            
            return s.val == t.val and helper(s.left, t.left) and helper(s.right, t.right)

        return helper(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


s = TreeNode(3)
s.left = TreeNode(4)
s.right = TreeNode(5)
s.left.left = TreeNode(1)
s.left.right = TreeNode(2)

t = TreeNode(4)
t.left = TreeNode(1)
t.right = TreeNode(2)
t.right.left = TreeNode(0)

s1 = TreeNode(3)
s1.left = TreeNode(4)
s1.right = TreeNode(5)
s1.left.left = TreeNode(1)
s1.left.right = TreeNode(2)
s1.left.right.left = TreeNode(0)

s2 = TreeNode(1)
s2.left = TreeNode(1)

print Solution().isSubtree(s, t)
print Solution().isSubtree(s1, t)
print Solution().isSubtree(s2, TreeNode(1))