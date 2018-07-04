# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    most = 0
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        data = {}
        def helper(root):
            if root == None: return
            if root.val not in data: data[root.val] = 0
            
            data[root.val] += 1
            if data[root.val] > self.most:
                self.most = data[root.val]

            helper(root.left)
            helper(root.right)

        results = []
        helper(root)
        for item in data.items():
            if item[1] == self.most:
                results.append(item[0])
        
        return results

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(2)

sol = Solution()
print sol.findMode(root)
print sol.findMode(None)
