class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        index = 0
        for i in reversed(range(len(s))):
        	o = ord(s[i]) - 64
        	num += (26 ** index) * o
        	index += 1
    	
    	return num
    	
sol = Solution()
print sol.titleToNumber("AAA")
