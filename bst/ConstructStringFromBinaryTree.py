# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """

        def preorder(t):
            if not t: return ''
            if not t.left and not t.right:
                return str(t.val) + ''
            if not t.right:
                return str(t.val) + '(' + preorder(t.left) + ')'
            return str(t.val) + '(' + preorder(t.left) + ')' + '(' + preorder(t.right) + ')'

        return preorder(t)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)

print Solution().tree2str(root) #1(2(4))(3)
print Solution().tree2str(root2) #1(2()(4))(3)