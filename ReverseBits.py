class Solution:
	# @param n, an integer
	# @return an integer
	def reverseBits(self, n):
		return int('{:032b}'.format(n)[::-1], 2)

	def reverseBits2(self, n):
		# res << 1: res/2
		# n & 1: 0 if n%2 == 0 else 1
		# n >>= 1: n = n / 2
		res = 0
		for i in xrange(32):
			res = (res << 1) + (n & 1)
			n >>= 1
		return res

sol = Solution()
print sol.reverseBits2(43261596)
