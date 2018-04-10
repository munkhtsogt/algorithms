class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return True if n % 4 != 0 else False


sol = Solution()
print sol.canWinNim(5)
