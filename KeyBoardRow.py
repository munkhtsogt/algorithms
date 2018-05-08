class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        r = []
        for w in words:
            c1, c2, c3 = 0, 0, 0
            for c in w:
                c = c.lower()
                if c in 'qwertyuiop':
                    c1 += 1
                elif c in 'asdfghjkl':
                    c2 += 1
                elif c in 'zxcvbnm':
                    c3 += 1
            
            if len(w) in [c1, c2, c3]:
                r.append(w)

        return r


print Solution().findWords(["Hello","Alaska","Dad","Peace"])
