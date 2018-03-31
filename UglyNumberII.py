class Solution(object):
    def nthUglyNumber(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		v = [1] * n
		t1 = t2 = t3 = 0
		for i in range(0, n - 1):
			v[i + 1] = min(v[t1] * 2, v[t2] * 3, v[t3] * 5)
			if v[i + 1] == v[t1] * 2:
				t1 += 1
			if v[i + 1] == v[t2] * 3:
				t2 += 1
			if v[i + 1] == v[t3] * 5:
				t3 += 1
		return v[n-1]
		
sol = Solution()
print sol.nthUglyNumber(10)
