class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        if len(p) == 0: return 0
        c = dict()
        s, ans = 0, 0
        c[p[0]] = 1
        for i in range(1, len(p)):
            c.setdefault(p[i], 1)
            if ord(p[i])-1 == ord(p[i-1]) or (p[i] == 'a' and p[i-1] == 'z'):
                c[p[i]] = max(c[p[i]], i-s+1)
            else:
                s = i 
        for i in c:
            ans += c[i]
        return ans
