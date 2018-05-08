import sys

class Solution(object):
    def shortestToChar(self, S, C):
		"""
		:type S: str
		:type C: str
		:rtype: List[int]
		"""

		dp = [0] * len(S)
		start = 0
		for i in range(len(S) - 1, -1, -1):
			if S[i] != C:
				start += 1
			else:
				break
				
		dp[len(S) - 1] = start
		for i in range(len(S) - 2, -1, -1):
			if S[i] != C:
				dp[i] = dp[i + 1] + 1
			else:
				dp[i] = 0
		
		for i in range(1, len(S)):
			if S[i] != C:
				dp[i] = min(dp[i], dp[i - 1] + 1) 
			else:
				dp[i] = 0
		
		return dp
        
        
print Solution().shortestToChar("loveleetcode", 'e')
