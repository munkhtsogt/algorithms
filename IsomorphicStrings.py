class Solution(object):
	def isIsomorphic(self, s, t):
		if len(s) != len(t): return False
		dic = {}
		for i in xrange(len(s)):
			print i
			if s[i] in dic:
				if dic[s[i]] != t[i]: return False
			else:
				if t[i] not in dic.values():
					dic[s[i]] = t[i]
				else:
					return False	
				
			
		return True
					
		
sol = Solution()

print sol.isIsomorphic("abab", "abba")
		
