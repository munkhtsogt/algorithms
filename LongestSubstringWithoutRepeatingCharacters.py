class Solution(object):
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		data = {}
		longest = count = 0
		for i in range(len(s)):
			if s[i] in data and count <= data[s[i]]:
				count = data[s[i]] + 1
			
			longest = max(longest, i - count + 1)
			data[s[i]] = i

		return longest	

	def lengthOfLongestSubstring2(self, s):

		arr = []
		longest = 0
		for i in range(len(s)):
			if s[i] not in arr:
				arr.append(s[i])
			else:
				longest = max(longest, len(arr))
				arr = arr[arr.index(s[i]) + 1:]
				arr.append(s[i])
				
		return max(longest, len(arr))	
        	
        	
        
sol = Solution()
print sol.lengthOfLongestSubstring2("abba")
