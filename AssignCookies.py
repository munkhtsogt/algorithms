class Solution(object):
    def findContentChildren(self, g, s):
		"""
		:type g: List[int]
		:type s: List[int]
		:rtype: int
		"""
		g.sort()
		s.sort()
		
		i, j = 0, 0
		while i < len(s) and j < len(g):
			if s[i] >= g[j]:
				j += 1
			i += 1
	
		return j
    	

print Solution().findContentChildren([10,9,8,7], [5,6,7,8])
