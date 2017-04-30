class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        counts = dict()
        m, n, start = len(s1), len(s2), -1
        for i in s1:
            counts.setdefault(i, 0)
            counts[i] += 1
        for end in range(n):
            if counts.get(s2[end], 0) > 0:
                counts[s2[end]] -= 1
            else:
                start += 1
                while start <= end and s2[start] != s2[end]:
                    if counts.has_key(s2[start]):
                        counts[s2[start]] += 1
                    start += 1
                
            if end - start == m:
                return True
        return False
