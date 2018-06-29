class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if not S or len(S) == 0: return [""]

        def permutation(S, result, index):
            if S not in result: result.append(S)
            if index == len(S): return

            for i in range(index, len(S)):
                if S[i].isalpha():
                    if S[i].islower():
                        c = S[i].upper()
                    else:
                        c = S[i].lower()
                    str = S[:i] + c + S[i + 1:]
                    permutation(str, result, i + 1)

            return result

        result = permutation(S, [], 0)
        return result

print Solution().letterCasePermutation('a1b2')