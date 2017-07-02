class Solution(object):
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 1000000007
        dp = [0, 0, 1, 2]
        for i in range(4, n+1):
            dp.append(((i-1)*(dp[i-1] + dp[i-2])) % x)
        return dp[n]
