class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        mydict = set(wordDict)
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(0, i):
                if dp[j] == 1 and s[j:i] in mydict:
                    dp[i] = 1
                    break
        return dp[n] == 1
        
