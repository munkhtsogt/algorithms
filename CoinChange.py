class Solution(object):
    def coinChange(self, coins, amount):
		"""
		:type coins: List[int]
		:type amount: int
		:rtype: int
		"""
		coins.sort()
		dp = [amount + 1] * (amount + 1)
		dp[0] = 0
		for i in range(1, amount + 1):
			for j in range(0, len(coins)): 	
				if i >= coins[j]:
					dp[i] = min(dp[i], dp[i - coins[j]] + 1)
		
		return  -1 if dp[amount] > amount else dp[amount]
		
print Solution().coinChange([2, 5, 10, 1], 27)
