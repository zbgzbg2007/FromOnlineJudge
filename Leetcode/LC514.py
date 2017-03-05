class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        n, m = len(ring), len(key)
        dp = [{} for i in range(m)]
        
        for i in range(n):
            if ring[i] == key[0]:
                dp[0][i] = min(i, n-i) + 1
        for i in range(1, m, 1):
            for j in dp[i-1]:
                for k in range(n):
                    if ring[k] == key[i]:
                        if k < j:
                            x = min(j - k, k + n - j) + 1 + dp[i-1][j]
                        else:
                            x = min(k - j, n - k + j) + 1 + dp[i-1][j]
                        if k in dp[i]:
                            dp[i][k] = min(dp[i][k], x)
                        else:
                            dp[i][k] = x
        ans = 10000000
        for i in dp[-1]:
            if ans > dp[-1][i]:
                ans = dp[-1][i]
        return ans
                    
