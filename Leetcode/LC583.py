class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        dp[0] = [i for i in range(n+1)]
        for i in range(m+1):
            dp[i][0] = i
        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[j-1] != word2[i-1]:
                    dp[j][i] = min(dp[j-1][i], dp[j][i-1])+1
                else:
                    dp[j][i] = dp[j-1][i-1]
        return dp[m][n]
