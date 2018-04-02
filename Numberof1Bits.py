class Solution(object):
	def hammingWeight(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		return '{:032b}'.format(n).count("1")
	
	def hammingWeight2(self, n):
		c = 0
		for _ in range(32):
			if n & 1 == 1:
				c += 1
			
			n >>= 1
			
		return c	

sol = Solution()
print sol.hammingWeight2(101)
