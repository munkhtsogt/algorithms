class Solution(object):
    def countAndSay(self, n):
		"""
		:type n: int
		:rtype: str
		"""
		st = "1"
		for i in range(1, n):
			count = 1
			f = st[0]
			r = ""
			for j in range(1, len(st)):
				if f == st[j]:
					count += 1	
				else:
					r += str(count) + f
					f = st[j]
					count = 1
			r += str(count) + f
			st = r
			
		return st
        

print Solution().countAndSay(10)
