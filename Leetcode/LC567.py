class Solution1(object):
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
   
class Solution2(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        a = [ord(x) - ord('a') for x in s1]
        b = [ord(x) - ord('a') for x in s2]
        
        t1 = [0] * 26
        for i in a:
            t1[i] += 1
        t2 = [0] * 26
        n = len(a)
        for i, x in enumerate(b):
            if i >= n:
                t2[b[i-n]] -= 1
            t2[x] += 1
            if t2 == t1:
                return True
        return False
