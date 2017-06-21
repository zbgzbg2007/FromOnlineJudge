class Solution(object):
    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        if a == 1: return a
        ans = ''
        m = 2**31
        for i in range(9, 1, -1):
            while a % i == 0:
                ans += str(i)
                a /= i
        ans = ans[::-1]
        if a != 1 or ans == '' or int(ans) >= m: return 0
        return int(ans)
                    
        
