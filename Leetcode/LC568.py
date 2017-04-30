class Solution(object):
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        n, k = len(days), len(days[0])
        dp = [[-1 for j in range(n)] for i in range(k)]
        for i in range(n):
            if flights[0][i] == 1 or i == 0:
                dp[0][i] = days[i][0]
        for i in range(1, k): 
            for j in range(n):
                if dp[i-1][j] >= 0:
                    for x in range(n):
                        if flights[j][x] == 1 or x == j:
                            dp[i][x] = max(dp[i][x], dp[i-1][j]+days[x][i])
        return max(dp[k-1])
