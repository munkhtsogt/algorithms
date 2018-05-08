# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def isBadVersion(v):
	bads = [5, 6, 7, 8]
	return v in bads

class Solution(object):
    def firstBadVersion(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		lo, hi = 1, n + 1
		while lo < hi:
			mid = lo + (hi - lo) / 2
			if not isBadVersion(mid):
				lo = mid + 1
			else:
				hi = mid

		return hi
		
print Solution().firstBadVersion(8)
    			
