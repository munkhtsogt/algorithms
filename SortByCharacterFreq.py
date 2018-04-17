class Solution(object):
    def frequencySort(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		freq = {}
		for c in s:
			if c not in freq:
				freq[c] = 1
			else:
				freq[c] += 1

		freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
		result = ""
		for p in freq:
			result += p[0] * p[1]
		
		return result
        
print Solution().frequencySort("Aabbccc")
