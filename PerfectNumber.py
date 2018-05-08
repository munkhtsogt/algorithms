class Solution(object):
    def checkPerfectNumber(self, num):
		"""
		:type num: int
		:rtype: bool
		"""
		if num <= 1: return False
		
		total = 1
		sqrt = int(num ** 0.5)
		for i in range(2, sqrt + 1):
			if num % i == 0:
				total += i + num / i

		return total == num
        
print Solution().checkPerfectNumber(14)
