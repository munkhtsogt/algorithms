class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B): return False
        if A == B and len(set(A)) < len(A): return True
        diff = []
        for a, b in zip(A, B):
            if a != b:
                diff.append((a, b))
        return len(diff) == 2 and diff[0] == diff[1][::-1]


sol = Solution()
print sol.buddyStrings("aa", "aa")