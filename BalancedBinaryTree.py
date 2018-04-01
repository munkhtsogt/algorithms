# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def traverse(root):
        	if root == None:
        		return 0
    		
    		l = traverse(root.left)
        	r = traverse(root.right)
        	
        	if l == -1 or r == -1 or abs(l - r) > 1:
        		return -1
        	
        	return 1 + max(l, r)	
        
        return traverse(root) != -1
