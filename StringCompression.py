class Solution(object):
    def compress(self, chars):
		"""
		:type chars: List[str]
		:rtype: int
		"""
		if len(chars) == 0: return 0
		
		chars.sort()
		f, count, r = chars[0], 1, 1
		for i in range(1, len(chars)):
			if f == chars[i]:
				count += 1
			else:
				f = chars[i]
				r += 1
				if count != 1:
					while count != 0:
						r += 1
						count /= 10
				count = 1
				
		if count != 1:
			while count != 0:
				r += 1
				count /= 10
						
		return r   
        
print Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])
