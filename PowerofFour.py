import math
class Solution(object):
    def isPowerOfFour(self, num):
		"""
		:type num: int
		:rtype: bool
		"""
		if num <= 0: return False
		r = math.log(num, 4)
		return math.ceil(r) == r
		
sol = Solution()
print sol.isPowerOfFour(15)
