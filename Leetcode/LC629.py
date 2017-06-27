class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        m = 1000000007
        dp = [[0 for i in range(k+1)] for j in range(n+1)]
        for i in range(n+1): dp[i][0] = 1
        for i in range(2, n+1):
            for j in range(1, k+1):
                dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % m 
                if j >= i: dp[i][j] -= dp[i-1][j-i]
                dp[i][j] = dp[i][j] % m
        return dp[n][k]
