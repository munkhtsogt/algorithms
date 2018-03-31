class Solution(object):
    def firstUniqChar(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		ch = []
		for c in set(s):
			if s.count(c) == 1:
				ch.append(s.index(c))		
		
		if len(ch) > 0:
			return min(ch)
		
		return -1
        
sol = Solution()
print sol.firstUniqChar("leetcode")
