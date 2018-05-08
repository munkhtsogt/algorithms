class Solution(object):
    def selfDividingNumbers(self, left, right):
		"""
		:type left: int
		:type right: int
		:rtype: List[int]
		"""
		r = []
		for i in range(left, right + 1):
			n, flag = i, True
			while n != 0:
				d = n % 10
				if d == 0 or i % d != 0:
					flag = False
					break	
				n /= 10
	
			if flag:
				r.append(i)

		return r
