class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        st = ""
        while n > 0:
        	n -= 1
        	st = chr(n % 26 + 65) + st
        	n /= 26
        	
        return st
        
sol = Solution()
print sol.convertToTitle(702)
