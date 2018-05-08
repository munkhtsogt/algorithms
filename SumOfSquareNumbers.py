class Solution(object):
    def judgeSquareSum(self, c):
		"""
		:type c: int
		:rtype: bool
		"""
		l = 0
		r = int(c ** 0.5)
		while l <= r:
			n = l * l + r * r
			if n == c: return True
			elif n > c: r -= 1
			else: l += 1
			
		return False	  
        
print Solution().judgeSquareSum(100)
