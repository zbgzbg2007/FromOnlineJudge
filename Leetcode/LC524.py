class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d = sorted(d)
        d = reversed(d)
        d = sorted(d, key = lambda x: len(x))
        d = reversed(d)
        for x in d:
            y = list(x)
            i, j, n, m = 0, 0, len(s), len(y)
            while i < m and j < n:
                if y[i] == s[j]:
                    i += 1
                if i == len(y):
                    return x
                j += 1
        return ""
    
