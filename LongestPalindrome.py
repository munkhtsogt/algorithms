class Solution(object):
    def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		data = {}
		for i in range(0, len(s)):
			if s[i] not in data:
				data[s[i]] = 1
			else:
				data[s[i]] += 1
		r, single = 0, 0
		for key in data:
			if data[key] % 2 == 0:
				r += data[key]
			else:
				r += data[key] - 1
				single = 1	
		
		return r + single
		
print Solution().longestPalindrome("")
        
