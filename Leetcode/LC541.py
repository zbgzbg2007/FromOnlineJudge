class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ss = list(s)
        n = len(ss)
        i = 0
        while n - i * k > 0:
            start, end = i * k, min(i * k + k, n)
            sub = ss[start:end]
            sub.reverse()
            for j in range(end-start):
                ss[start + j] = sub[j]
            i += 2
        return ''.join(ss)
