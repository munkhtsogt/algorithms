# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        s = set()
        def preorder(root):
            if not root: return

            s.add(root.val)

            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        if len(s) < 2: return -1
        s = sorted(list(s))
        return s[1]



root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

root2 = TreeNode(2)
root2.left = TreeNode(2)
root2.right = TreeNode(2)

root3 = TreeNode(5)
root3.left = TreeNode(8)
root3.right = TreeNode(5)

print Solution().findSecondMinimumValue(root)
print Solution().findSecondMinimumValue(root2)
print Solution().findSecondMinimumValue(root3)