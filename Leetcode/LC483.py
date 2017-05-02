class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        n = int(n)
        for b in range(64, 0, -1):
            l, r = 2, n+1
            while l <= r:
                m = (r-l)/2 + l
                x = 0
                for i in range(b):
                    x += m**i
                    if x > n:
                        break
                if x == n:
                    return str(m)
                if x > n: r = m - 1
                else: l = m + 1
        return str(n+1)
        
