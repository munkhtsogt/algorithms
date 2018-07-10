class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s, t = [], []
        for c in S:
            if c != '#': s.append(c)
            elif len(s) != 0: s.pop()
        
        for c in T:
            if c != '#': t.append(c)
            elif len(t) != 0: t.pop()
        
        return "".join(s) == "".join(t)



sol = Solution()  
print sol.backspaceCompare("ab#c", "ad#c")
print sol.backspaceCompare("ab##", "c#d#")
print sol.backspaceCompare("a#c", "b")
print sol.backspaceCompare("a##c", "#a#c")
print sol.backspaceCompare("isfcow#", "isfco#w#")