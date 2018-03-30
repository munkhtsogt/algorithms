class Solution(object):
    def isPalindrome(self, x):
		if x < 0: return False
		rev = 0
		y = x
		while x != 0:
			rev = rev * 10 + x % 10
			x /= 10

		return y == rev

sol = Solution()
print sol.isPalindrome(1001)
