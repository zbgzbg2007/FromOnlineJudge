class Solution(object):
    def splitLoopedString(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = ''.join(strs)
        n = len(strs)
        for i in range(n):
            strs[i] = max(strs[i], strs[i][::-1])
        for i in range(n):
            for j in range(len(strs[i])):
                t = max(strs[i][j:], strs[i][::-1][j:])
                t += ''.join(strs[i+1:]+strs[:i])
                if strs[i][j:] > strs[i][::-1][j:]:
                    t += strs[i][:j]
                else:
                    t += strs[i][::-1][:j]
                ans = max(ans, t)
        return ans
                    
                
