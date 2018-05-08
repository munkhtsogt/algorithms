class Solution(object):
	def convertToTitle(self, n):
		"""
		:type n: int
		:rtype: str
		"""
		r = ""
		while n != 0:
			n -= 1
			r = chr(n % 26 + ord('A')) + r
			n /= 26

		return r

	def titleToNumber(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		num, j = 0, 0
		for i in range(len(s) - 1, -1, -1):
			o = ord(s[i]) - 64
			num += (26 ** j) * o
			j += 1
	
	
		return num	
	
        		
	

print Solution().titleToNumber('AAA')        


