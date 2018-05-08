class Solution(object):
    def constructRectangle(self, area):
		"""
		:type area: int
		:rtype: List[int]
		"""

		i = int(area ** 0.5)
		
		if i * i == area: 
			return [i, i]

		while area % i != 0:
			i -= 1
		
		return [int(area/i), i]		
		
		

print Solution().constructRectangle(24)
