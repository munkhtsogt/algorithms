import sys
class Solution(object):
    def flipgame(self, fronts, backs):
		"""
		:type fronts: List[int]
		:type backs: List[int]
		:rtype: int
		"""
		dups = []
		for i in range(len(fronts)):
			if fronts[i] == backs[i]:
				dups.append(fronts[i])
		
		r = sys.maxint
		for	f in fronts:
			if f not in dups:
				r = min(r, f)		
		
		for	b in backs:
			if b not in dups:
				r = min(r, b)
		
		return 0 if r == sys.maxint else r
        	
         
        
print Solution().flipgame([1,2,4,4,7], [1,3,4,1,3])
