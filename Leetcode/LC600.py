class Solution(object):
    def findIntegers(self, num):
        """ 
        :type num: int
        :rtype: int
        """
        b = bin(num)[2:]
        n = len(b)
        dp = [[1, 1] for i in range(n+1)] 
        for i in range(2, n+1):
            dp[i][0] = dp[i-1][0] + dp[i-1][1]
            dp[i][1] = dp[i-1][0]
        ans = 0
        for i in range(n):
            if b[i] == '1':
                ans += dp[n-i][0]
                if i-1 >= 0 and b[i-1] == '1':
                    break
        if b.find('11') == -1:
            ans += 1
        return ans
        
