class Solution(object):
	def countPrimes(self, n):
		if n < 2: return 0
		isPrimes = [True] * n
		isPrimes[0] = isPrimes[1] = False
		for i in range(0, int(n ** 0.5) + 1):
			if isPrimes[i]:
				j = i * i
				while j < n:
					isPrimes[j] = False
					j += i
					
		return len(filter(lambda x: x == True, isPrimes))
			
sol = Solution()
print sol.countPrimes(0)
		
