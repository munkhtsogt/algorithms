class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if l == 0: return ""
        return s[l-1] + self.reverseString(s[0:l-1])
    
    def reverseStringPythonic(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
        
    
    def reverseStringStack(self, s):
		stack = []

		for c in s:
			stack.append(c)

		r = ''
		while len(stack) != 0:
			r += stack[-1]
			stack.pop()
		return r
	
sol = Solution()
print sol.reverseStringStack("hello world")
