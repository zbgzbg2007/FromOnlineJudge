class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        nums = []
        for i in range(len(strs)):
            nums.append([0, 0])
            for x in strs[i]:
                if x == '0': nums[i][0] += 1
                else: nums[i][1] += 1
        ans = 0
        for k in range(len(strs)):
            for i in range(m+1):
                for j in range(n+1):
                    if i + nums[k][0] <= m and j + nums[k][1] <= n:
                        dp[i][j] = max(dp[i][j], dp[i+nums[k][0]][j+nums[k][1]]+1)
        return max(max(dp))
        
