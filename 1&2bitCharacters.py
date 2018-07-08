class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i, size = 0, len(bits)
        while i < size - 1:
            i += bits[i] + 1

        return i == size - 1

sol = Solution()
print sol.isOneBitCharacter([1, 0, 0])
print sol.isOneBitCharacter([1, 1, 1, 0])