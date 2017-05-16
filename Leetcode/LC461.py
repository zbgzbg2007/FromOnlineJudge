class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        a, b = format(x, '032b'), format(y, '032b')
        ans = 0
        for i in range(32):
            if a[i] != b[i]: ans += 1
        return ans
        
