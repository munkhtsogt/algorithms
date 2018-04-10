class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(" ")
        if len(pattern) != len(words): return False
        
        data = {}
        for i in range(0, len(pattern)):
        	if pattern[i] not in data:
        		if words[i] in data.values():
        			return False
        		data[pattern[i]] = words[i]
    		elif data[pattern[i]] != words[i]:
    			return False	
				
        return True
        

sol = Solution()
print sol.wordPattern("abba", "cat dog dog cat")
