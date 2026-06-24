class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = ""
        e = max(len(word1), len(word2))  
        i = 0

        while i < e:
            if i < len(word1):   
                res += word1[i]
            if i < len(word2):   
                res += word2[i]
            i += 1

        return res