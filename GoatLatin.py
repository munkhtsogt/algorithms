class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """

        vowels = ['a', 'e', 'i', 'o', 'u']
        words = S.split(' ')
        for i in range(0, len(words)):
            if words[i][0].lower() not in vowels:
                words[i] = words[i][1:] + words[i][0]
            
            words[i] += 'ma' + (i + 1) * 'a'
        
        return ' '.join(words)

            


print Solution().toGoatLatin("The quick brown fox jumped over the lazy dog")