class Solution(object):
	def canConstruct(self, ransomNote, magazine):
		"""
		:type ransomNote: str
		:type magazine: str
		:rtype: bool
		"""
		data = {}
		for c in magazine:
			if c not in data:
				data[c] = 1
			else:
				data[c] += 1
			
		for c in ransomNote:
			if c not in data:
				return False
			else:
				if data[c] != 0:
					data[c] -= 1
				else:
					return False

		return True

	def canConstruct2(self, ransomNote, magazine):
	
		for i in set(ransomNote):
			if ransomNote.count(i) > magazine.count(i):
				return False
		return True
        
print Solution().canConstruct2("aa", "aab")
