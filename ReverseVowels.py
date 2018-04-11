class Solution(object):
    def reverseVowels(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		vowels = ['a', 'e', 'i', 'o', 'u']
		s = list(s)
		l, r = 0, len(s) - 1
		while l < r:
			if s[l].lower() not in vowels:
				l += 1
			elif s[r].lower() not in vowels:
				r -= 1	
			else:
				s[l], s[r] = s[r], s[l]
				l += 1
				r -= 1
		return ''.join(s)
				
		
sol = Solution()
print sol.reverseVowels("hello")
print sol.reverseVowels("leetcode")
print sol.reverseVowels("aA")
print sol.reverseVowels("race car")
