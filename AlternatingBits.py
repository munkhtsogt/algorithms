class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        tmp = n
        c = 0
        while tmp != 0:
        	c += 1
        	tmp /= 2
    	
    	tmp = n ^ (2 ** c  - 1)
    	return tmp == n / 2

print Solution().hasAlternatingBits(7)
