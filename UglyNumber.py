class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
    	for factor in [2, 3, 5]:
    		while num % factor == 0 and num > 0:
    			num /= factor
    			
    	return num == 1				 	
	
sol = Solution()
print sol.isUgly(14)
